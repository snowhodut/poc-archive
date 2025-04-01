from flask import Flask, request, render_template_string

app = Flask(__name__)

# 플래그 값 (실제로는 노출되면 안 되는 민감한 정보)
FLAG = "FLAG{XSS_SUCCESSFULLY_EXPLOITED}"

@app.route("/")
def index():
    q = request.args.get("q", "")
    
    # 템플릿 직접 렌더링 (render_template_string을 사용해 단일 파일로 구성)
    template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>XSS Demo</title>
    </head>
    <body>
        <h1>검색 결과</h1>
        <p>입력한 검색어: {{ q | safe }}</p>
    </body>
    </html>
    '''
    
    return render_template_string(template, q=q)

@app.route("/flag")
def flag():
    return f"<script>alert('{FLAG}')</script>"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)

