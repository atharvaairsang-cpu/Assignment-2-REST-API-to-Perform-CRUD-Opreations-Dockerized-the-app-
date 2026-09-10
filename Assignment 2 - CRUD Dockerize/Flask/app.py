from flask import Flask, request, jsonify

from create import create_user
from read import get_users, get_user
from update import update_user
from delete import delete_user

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello, Flask app is running inside Docker!"


@app.route('/users', methods=['POST'])
def create_user_route():
    create_user(request.json)
    return jsonify({"message": "User created"}), 201


@app.route('/users', methods=['GET'])
def get_users_route():
    return jsonify(get_users())


@app.route('/users/<int:id>', methods=['GET'])
def get_user_route(id):
    user = get_user(id)
    if user is None:
        return jsonify({"error": "Not found"}), 404
    return jsonify(user)


@app.route('/users/<int:id>', methods=['PUT'])
def update_user_route(id):
    update_user(id, request.json)
    return jsonify({"message": "User updated"})


@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user_route(id):
    delete_user(id)
    return jsonify({"message": "User deleted"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
