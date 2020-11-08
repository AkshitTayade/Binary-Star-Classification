import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

class StarClassification:
    def __init__(self):
        pass

    def clean_dataset(self):
        dataset = pd.read_csv('dataset_types_star.csv')
        dataset.drop('Star color', axis=1, inplace=True)
        self.encoder = LabelEncoder()
        dataset['Spectral Class'] = self.encoder.fit_transform(dataset['Spectral Class'])
        Y = dataset.iloc[:, 4]
        dataset.drop(['Star type'], axis=1, inplace=True)
        X = dataset
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(X, Y, test_size=0.20, random_state=0)

    def star_type(self, i):
        if i == 0:
            return('Brown Dwarf')
        
        elif i == 1:
            return('Red Dwarf')
            
        elif i == 2:
            return('White Dwarf')
            
        elif i == 3:
            return('Main Sequence')
            
        elif i == 4:
            return('Supergiant')
            
        elif i == 5:
            return('Hypergiant')

    def RandomForest(self):
        self.rf = DecisionTreeClassifier()
        self.rf.fit(self.x_train, self.y_train)

    def UserPrediction(self, temp, lumin, radi, mag, sc):
        temperature = int(temp)
        #9940
        luminosity = (float(lumin)*3.828*10**26)/(3.828*10**26)
        #25.4
        radius = (float(radi))/(6.9551*10**8)
        #1.19*10**6
        magnitude = float(mag)
        #1.42
        spectral_class = self.encoder.transform([sc])
        #'A'    

        user_inp = [temperature, luminosity, radius, magnitude, spectral_class]
        
        y_user_pred = self.rf.predict([user_inp])
        return(self.star_type(y_user_pred))


