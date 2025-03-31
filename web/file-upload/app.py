# File Upload 기본 실습용 app.py
from flask import Flask, request, redirect, url_for, render_template_string
import os

UPLOAD_FOLDER = './uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return '<h3>Go to <a href="/upload">/upload</a> to test file upload</h3>'

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files.get('file')
        if file:
            path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(path)
            return f"Upload success! File saved as: {file.filename}"
        return "No file uploaded"

    return render_template_string('''
        <h2>Upload a file</h2>
        <form method="POST" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit" value="Upload">
        </form>
    ''')

if __name__ == '__main__':
    app.run(debug=True, port=3000)