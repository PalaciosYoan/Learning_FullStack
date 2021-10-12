from flask import *
import requests
import json

app = Flask(__name__, template_folder='.')


@app.route('/')
def homepage():

    r = requests.get('https://amhep.pythonanywhere.com/grades')
    
    return r.json()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)