# WAF 우회 SQLi - app.py
from flask import Flask, request
import sqlite3
import re

app = Flask(__name__)

conn = sqlite3.connect(':memory:', check_same_thread=False)
cursor = conn.cursor()
cursor.execute("CREATE TABLE users (username TEXT, password TEXT)")
cursor.execute("INSERT INTO users VALUES ('admin', 'adminpass')")
conn.commit()

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # WAF 필터링: 기본적인 키워드 차단
    if any(keyword in username.lower() for keyword in ['or', 'and', '=', '--']):
        return "WAF 차단: forbidden keyword detected"

    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print("[DEBUG]", query)
    try:
        result = cursor.execute(query).fetchone()
        if result:
            return "FLAG{WAF_BYPASS_SUCCESS}"
        return "Login failed"
    except:
        return "SQL Error"

app.run(debug=True, port=3000)