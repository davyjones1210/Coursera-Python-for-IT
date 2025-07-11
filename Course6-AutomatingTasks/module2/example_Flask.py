# This is not an excutable code block
from flask import Flask

app = Flask(__name__)

@app.route('/hello/<name>')
def hello_world(name):
    return f'Hello, {name}!'