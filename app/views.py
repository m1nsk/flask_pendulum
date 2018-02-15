from app.app import app
from flask import request
import time


@app.route('/')
@app.route('/index')
def index():
    if request.method == "GET":
        while True:
            time.sleep(10000)
            print("hello")
        return "Hello, Wqqqorld!"
    return "Waba-duba-da!"
