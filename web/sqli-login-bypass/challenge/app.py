from flask import Flask, request, redirect, render_template, make_response
import pymysql.cursors
import os
import secrets

app = Flask(__name__)

# 환경변수에서 DB 정보 가져오기
def db():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="1234",
        database=os.environ.get("MYSQL_DATABASE", "chall"),
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

import secrets

def insert_flag():
    conn = None
    try:
        admin_password = secrets.token_hex(8)
        print(f"[DEBUG] admin password: {admin_password}")  # 실제 서비스에서는 출력 안함!

        with open("./flag.txt") as f:
            flag = f.read().strip()

        conn = db()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE username = 'admin'")
            if not cursor.fetchone():
                cursor.execute("INSERT INTO users (username, password) VALUES ('admin', %s)", (admin_password,))
                cursor.execute("INSERT INTO flag (username, value) VALUES ('admin', %s)", (flag,))
                conn.commit()

    except Exception as e:
        print(f"[!] Flag 삽입 실패: {e}")
    finally:
        if conn:
            conn.close()



BLACKLIST = [
    "\"", "--", "#", "/*", "*/",
    " or ", " and ", "union", "select",
    "insert", "update", "delete"
]

def check_waf(value):
    value = value.lower()
    return any(keyword in value for keyword in BLACKLIST)

@app.route("/")
def index():
    username = request.cookies.get("username")
    if not username:
        return redirect("/login")
    return render_template("chat.html", username=username)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            return "Missing required parameters", 400

        if len(username) > 64 or len(password) > 64:
            return "Too long!", 400

        if check_waf(username) or check_waf(password):
            return "Alien Warning: Don't u ever try SQL injection 🔫👽", 400
        
        conn = None

        try:
            conn = db()
            with conn.cursor() as cursor:
                query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
                cursor.execute(query)
                user = cursor.fetchone()
        except Exception as e:
            return f"DB error: {e}", 500
        finally:
            if conn:
              conn.close()

        if not user:
            return "Invalid credentials", 403

        resp = make_response(redirect("/"))
        resp.set_cookie("username", user["username"])
        return resp

    return render_template("index.html")

@app.route("/flag")
def flag():
    username = request.cookies.get("username")
    if not username:
        return redirect("/login")

    try:
        conn = db()
        with conn.cursor() as cursor:
            query = f"SELECT value FROM flag WHERE username = '{username}'"
            cursor.execute(query)
            result = cursor.fetchone()
    except Exception as e:
        return f"DB error: {e}", 500
    finally:
        conn.close()

    if result:
        return f"<h3>FLAG: {result['value']}</h3>"
    return "No flag for u ㅋㅋ! 👽"

if __name__ == "__main__":
    insert_flag()
    app.run(host="0.0.0.0", port=3000, debug=True)
