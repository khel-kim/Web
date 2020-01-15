from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return "Index!"


@app.route('/hello/')
def hello():
    return "Hello World!"


@app.route('/members/')
def members():
    return "Members"


@app.route('/members/<string:name>/')
def get_member(name):
    return f"The name is {name}"


if __name__ == "__main__":
    app.run()