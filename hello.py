from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.route("/rohan")
def rohan():
    return "popat rohan"

# flask --app hello run --reload