from app import app
from flask import render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('index.html')
    if request.method == "POST":
        if 'image' not in request.files:
            print('No file part')
            return redirect(request.url)
        file = request.files['image']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        print(file.filename)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            return redirect(request.url)
        return "Success"

