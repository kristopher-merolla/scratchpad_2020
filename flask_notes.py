##########################
## -- Notes on Flask -- ##
##########################

# Flask can be used to make a web server and is quick and easy to setup

# Installation

pip3 install Flask

# Will be using a virtual env so do pip3 install virtualenv https://pypi.org/project/virtualenv/

# Start up the virtual env
virtualenv flask
cd flask
source bin/activate

# For flask 1.0.2

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!" 

# Do not run in app, run with:
# FLASK_APP=hello.py flask run

##########################

# https://stackoverflow.com/questions/31252791/flask-importerror-no-module-named-flask
