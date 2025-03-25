from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    q = request.args.get("q", "")
    return render_template("index.html", q=q)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
