# A very simple website we can spin up with flask. By default it's running on 127.0.0.1 and port 8000 but you can change it below.

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to my website!"

app.run(host='0.0.0.0', port='8000')