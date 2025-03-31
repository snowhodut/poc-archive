# SSRF 기본 실습용 app.py
from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return '<h3>Use /fetch?url= to test SSRF</h3>'

@app.route('/fetch')
def fetch():
    url = request.args.get('url')
    if not url:
        return "Missing URL"
    try:
        res = requests.get(url, timeout=2)
        return res.text[:200]  # 응답 일부만 반환
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True, port=3000)