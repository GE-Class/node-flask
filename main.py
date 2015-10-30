from flask import Flask, request, json, jsonify
app = Flask(__name__)

import sys
sys.path.append('.')
from user import User

@app.route("/hello", methods=['GET'])
def hello():
    return "world"

@app.route("/users/<id>/money", methods=['GET'])
def money(id):
    rows = User.money(id)
    total = 0
    for row in rows:
        total += row[2]
    t = {'total': str(total)}
    print(t)
    return jsonify(t=t)

@app.route("/sum", methods=['POST'])
def sum():
    data = request.get_json()
    x = int(data['x'])
    y = int(data['y'])
    data['sum'] = x + y
    return jsonify(data=data)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
