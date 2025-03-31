# SQLi Login Bypass Challenge - app.py (CTF-style)
from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)

with open('/flag.txt') as f:
    FLAG = f.read().strip()

# DB 초기화 (파일 기반으로 보존 가능하게)
DB_FILE = 'challenge.db'
if os.path.exists(DB_FILE):
    os.remove(DB_FILE)

conn = sqlite3.connect(DB_FILE, check_same_thread=False)
cursor = conn.cursor()
cursor.execute("CREATE TABLE users (username TEXT, password TEXT)")
cursor.execute("INSERT INTO users VALUES ('admin', 'supersecret')")
cursor.execute("INSERT INTO users VALUES ('guest', 'guest')")
conn.commit()

@app.route('/')
def index():
    return '<h3>Go to <a href="/login">/login</a> to login</h3>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        print("[DEBUG]", query)

        try:
            result = cursor.execute(query).fetchone()
            if result and result[0] == 'admin':
                return f"Welcome, admin! {FLAG}"
            elif result:
                return f"Welcome, {result[0]}! But no flag for you. ㅋㅋ!"
            else:
                return "Login failed!"
        except:
            return "Query error"

    return '''
        <h2>Login</h2>
        <form method="POST">
            Username: <input name="username"><br>
            Password: <input name="password" type="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
