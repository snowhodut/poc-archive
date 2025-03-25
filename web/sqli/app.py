from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# SQLite 메모리 DB, 테스트용 계정 생성
def init_db():
    conn = sqlite3.connect(':memory:', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (username TEXT, password TEXT)")
    cursor.execute("INSERT INTO users VALUES ('admin', 'adminpass')")
    conn.commit()
    return conn


db = init_db()

# 로그인 페이지 라우트
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        print(f"[DEBUG] SQL Query: {query}")
        cursor = db.cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        if result:
            return "Welcome, admin!"
        else:
            return "Login failed!"
    return render_template_string('''
        <h2>Login</h2>
        <form method="post">
            Username: <input name="username"><br>
            Password: <input name="password" type="password"><br>
            <input type="submit" value="Login">
        </form>
    ''')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
