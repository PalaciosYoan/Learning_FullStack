from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import json
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Grades(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    grade = db.Column(db.Float, unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name

        
@app.route('/')
def index():
    data = Grades.query.all()
    json_data = json.loads("{}")
    for name in data:
        c = "%s" % json.dumps(name.name)
        new_data = {name.name:name.grade}
        
        print(new_data)
        json_data.update(new_data)
    print(json_data)
    return jsonify(json_data)


app.run(debug=True)