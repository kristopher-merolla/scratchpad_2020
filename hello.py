
# For flask 1.0.2

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!" 

# Do not run in app, run with:
# FLASK_APP=hello.py flask run