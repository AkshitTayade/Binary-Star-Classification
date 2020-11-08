from model import StarClassification
from flask import Flask, request, render_template, url_for

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = 'akshittayade'

@app.route('/')
def index():
    return(render_template('index.html'))

@app.route('/result', methods=['GET', 'POST'])
def prediction():

    star = StarClassification()
    star.clean_dataset()
    star.RandomForest()

    if request.method == 'POST':
        temp = request.form['temp']
        lumin = request.form['lumin']
        radi = request.form['radi']
        mag = request.form['mag']
        sc = request.form['sc']
        
        user_value_predicted = star.UserPrediction(temp, lumin, radi, mag, sc.upper())

        img_path = "../static/"

        if user_value_predicted == 'Brown Dwarf':
            img_path = img_path + "brown_dwarf.png"
        
        elif user_value_predicted == 'Red Dwarf':
            img_path = img_path + "red_dwarf.jpg"
        
        elif user_value_predicted == 'White Dwarf':
            img_path = img_path + "white_dwarf.png"

        elif user_value_predicted == 'Main Sequence':
            img_path = img_path + "main_sequence.jpeg"

        elif user_value_predicted == 'Supergiant':
            img_path = img_path + 'supergiant.jpg'

        else:
            img_path = img_path + "hypergiant.jpg"

        return(render_template('index.html', img_path=img_path, prediction=user_value_predicted))
    
    return(render_template('index.html'))

if __name__ == "__main__":
    app.run()


