import os
from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)
# 데모용: 게시물(댓글) 저장을 위한 메모리 리스트
posts = []

@app.route("/", methods=["GET", "POST"])
def index():
    global posts
    if request.method == "POST":
        # 사용자가 입력한 값을 그대로 명령어 인자로 사용 (취약점 존재)
        user_input = request.form.get("post", "")
        # 기본 명령어: ls
        # 사용자 입력이 제대로 검증되지 않으므로, 예를 들어 "; cat /etc/passwd" 등의 페이로드를 주면
        # ls 명령어 외에 추가 명령어가 실행될 수 있습니다.
        command = "ls " + user_input
        try:
            # os.popen()을 사용해 명령어 실행 결과를 캡처합니다.
            output = os.popen(command).read()
        except Exception as e:
            output = str(e)
        # 명령어 실행 결과를 게시물로 저장 (이스케이프 없이 출력)
        posts.append(output)
        return redirect(url_for("index"))
    
    template = '''
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="UTF-8">
      <title>Command Injection Demo</title>
    </head>
    <body>
      <h1>디렉토리 정보 조회 (Command Injection Demo)</h1>
      <form method="POST">
        <!-- 사용자가 입력한 값이 그대로 ls 명령어의 인자로 사용됩니다. -->
        <input type="text" name="post" placeholder="인자 입력 (예: / 또는 ; cat /etc/passwd)" size="50">
        <input type="submit" value="실행">
      </form>
      <hr>
      <h2>실행 결과 (게시물)</h2>
      <ul>
        {% for p in posts %}
          <li>{{ p | safe }}</li>
        {% endfor %}
      </ul>
    </body>
    </html>
    '''
    return render_template_string(template, posts=posts)

if __name__ == "__main__":
    app.run(debug=True, port=3000)
