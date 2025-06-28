
from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy in-memory data
users = [
    {"id": 1, "name": "Alice", "role": "Engineer"},
    {"id": 2, "name": "Bob", "role": "Data Scientist"}
]

@app.route('/')
def home():
    return "Dummy API is running!"

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    return jsonify(user) if user else ("User not found", 404)

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    users.append(data)
    return jsonify(data), 201

if __name__ == '__main__':
    app.run(debug=True)
