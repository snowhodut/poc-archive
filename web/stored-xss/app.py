from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)
# 메모리에 저장된 댓글 리스트 (데모용)
comments = []

@app.route("/", methods=["GET", "POST"])
def index():
    global comments
    if request.method == "POST":
        # 사용자로부터 댓글을 입력받아 저장 (입력 값에 대한 검증이나 이스케이프 없음)
        comment = request.form.get("comment", "")
        comments.append(comment)
        return redirect(url_for("index"))
    
    # GET 요청 시 저장된 댓글을 그대로 보여줌 (초기화하지 않음)
    template = '''
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="UTF-8">
      <title>Stored XSS Demo</title>
    </head>
    <body>
      <h1>댓글 남기기 (Stored XSS Demo)</h1>
      <form method="POST">
        <textarea name="comment" rows="4" cols="50" placeholder="댓글을 입력하세요"></textarea><br>
        <input type="submit" value="댓글 등록">
      </form>
      <hr>
      <h2>저장된 댓글</h2>
      <ul>
        {% for c in comments %}
          <!-- | safe 를 사용해 이스케이프 처리를 하지 않으므로, XSS 페이로드가 그대로 실행됩니다. -->
          <li>{{ c | safe }}</li>
        {% endfor %}
      </ul>
    </body>
    </html>
    '''
    return render_template_string(template, comments=comments)

if __name__ == "__main__":
    app.run(debug=True, port=3000)
