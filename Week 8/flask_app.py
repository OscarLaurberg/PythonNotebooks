#!flask/bin/python
from flask import Flask, jsonify, abort, request
import sqlalchemy as s_a


SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:root@db/db"
engine = s_a.create_engine(SQLALCHEMY_DATABASE_URL)
connection = engine.connect()
query = 'select * from python'
ResultProxy = connection.execute(query)
python = ResultProxy.fetchall()
query = 'select * from js'
ResultProxy = connection.execute(query)
js = ResultProxy.fetchall()
query = 'select * from java'
ResultProxy = connection.execute(query)
java = ResultProxy.fetchall()

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': 'Go shopping',
        'description': 'Milk, Cheese, Fruit, Wine', 
        'done': False
    },
    {
        'id': 2,
        'title': 'Study',
        'description': 'Learn about uWsgi server and flask with python', 
        'done': False
    }
]


@app.route('/todo/api/python', methods=['GET'])
def get_python():
    
    return jsonify({'Python': [dict(row) for row in python]})

@app.route('/todo/api/js', methods=['GET'])
def get_js():
    
    return jsonify({'JS': [dict(row) for row in js]})

@app.route('/todo/api/java', methods=['GET'])
def get_java():
    
    return jsonify({'Java': [dict(row) for row in java]})


if __name__ == '__main__':
    app.run(debug=True)

