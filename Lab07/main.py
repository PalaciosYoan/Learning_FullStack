from flask import Flask, render_template, jsonify, request, redirect
import json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='.')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)

class Grades(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    grade = db.Column(db.Float, unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name

def to_json(student_data):
    try:
        json_data = json.loads("{}")
        for student in student_data:
            json_data.update({student.name:student.grade})
    except:
        json_data = json.loads("{}")
        json_data.update({student_data.name:student_data.grade})
    return json_data

@app.route('/')
def default():
    return '''
            Grading app Manager...
            (/home) <-- for web app
            (/grade) <-- for API
            '''

def get_all_students():
    return Grades.query.all()

@app.errorhandler(404)
def page_not_found(error):
    return "error", 404

@app.route('/grade', methods=['GET', 'POST', 'PUT', 'DELETE'])
def api():
    '''handles GET and POST'''
    all_students_data = get_all_students()
    json_data = to_json(all_students_data)
    if request.method == 'GET':
        json_data = to_json(all_students_data)
    
    elif request.method == 'POST':
        new_data = request.get_json()
        name = new_data['name']
        grade = new_data['grade']
        if name in json_data:
            return page_not_found(404)
        new_student = Grades(name=name, grade=grade)
        db.session.add(new_student)
        db.session.commit()

    return jsonify(json_data)

@app.route('/grade/<string:name>', methods=['GET', 'PUT', 'DELETE'])
def apiSpecificName(name):
    '''handle GET PUT DELETE for specifics names'''
    students_data = Grades.query.filter_by(name=name).first()
    json_data = to_json(students_data)
    if request.method == 'GET':
        if name in json_data:
            return jsonify(
                            {
                                name:json_data[name]
                            }
            )
        return jsonify({})
    elif request.method == 'PUT':
        if name in json_data:
            new_grade = request.get_json()
            grade = new_grade['grade']
            students_data.grade = grade
            db.session.commit()
    elif request.method == 'DELETE':
        if name in json_data:
            Grades.query.filter_by(name=name).delete()
            db.session.commit()
    
    return jsonify(json_data)

@app.route('/home')
def homepage():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105, debug=True)