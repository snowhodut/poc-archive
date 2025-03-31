# IDOR 기본 실습용 app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

users = {
    "1": {"username": "guest", "email": "guest@example.com"},
    "2": {"username": "admin", "email": "admin@example.com", "flag": "FLAG{IDOR_ACCESS_GRANTED}"}
}

@app.route('/')
def index():
    return '<h3>Try accessing /profile/&lt;user_id&gt;</h3>'

@app.route('/profile/<user_id>')
def profile(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return "User not found", 404

if __name__ == '__main__':
    app.run(debug=True, port=3000)
