from flask import Flask
from werkzeug.contrib.fixers import ProxyFix
app = Flask(__name__)
from flask import request
import time


@app.route('/')
@app.route('/index')
def index():
    if request.method == "GET":
        for i in range(4):
            time.sleep(3)
            print(i, "hello")
        return "Hello, Wqqqorld!"
    return "Waba-duba-da!"


app.wsgi_app = ProxyFix(app.wsgi_app)
if __name__ == "__main__":
    app.run()
