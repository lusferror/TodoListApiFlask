from flask import Flask
from flask import jsonify
from flask import request
import json

app = Flask(__name__)

todos = [{"label":"my first task", "done":False}]

@app.route('/todo')
def hello_world():
    return "<h1>Hello!</h1>"

@app.route('/todos',methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body= request.json
    todos.extend(request_body)
    print("Incoming request with the following body", request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    try:
        print("This is the position to delete: ",position)
        del(todos[position])
        return jsonify(todos)
    except Exception as e:
        return jsonify(todos)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=3245, debug =True)