from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__, template_folder='.')

@app.route('/')
def default():
    return '''
            Grading app Manager...
            (/home) <-- for web app
            (/grade) <-- for API
            '''


@app.route('/grade', methods=['GET', 'POST', 'PUT', 'DELETE'])
def api():
    '''handles GET and POST'''
    f = open('db.txt', 'r+')
    if request.method == 'GET':
        json_data = json.load(f)
    elif request.method == 'POST':
        print('entering post')
        f = open('db.txt', 'r+')
        json_data = json.load(f)
        f.seek(0)
        new_data = request.get_json()
        name = new_data['name']
        grade = new_data['grade']
        json_data.update({name:grade})
        print(json_data)

        f.write(json.dumps(json_data))
        f.truncate()
        
    f.close()
        
    return jsonify(json_data)

@app.route('/grade/<string:name>/', methods=['GET', 'PUT', 'DELETE'])
def apiSpecificName(name):
    '''handle GET PUT DELETE for specifics names'''
    f = open('db.txt', 'r+')
    json_data = json.load(f)
    f.seek(0)
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
            new_data = request.get_json()
            name = new_data['name']
            grade = new_data['grade']
            json_data[name] = grade
    elif request.method == 'DELETE':
        if name in json_data:
            del json_data[name]
    
    f.write(json.dumps(json_data))
    f.truncate()
    f.close()
    return jsonify(json_data)

@app.route('/home')
def homepage():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105, debug=True)