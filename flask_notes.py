##########################
## -- Notes on Flask -- ##
##########################

# Flask can be used to make a web server and is quick and easy to setup

# Installation
pip3 install Flask

# Will be using a virtual env so do pip3 install virtualenv https://pypi.org/project/virtualenv/

##########################
## Getting Flask to Run ##
##########################

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

##########################

# Templating (Views)

# Flask uses a templating engine called Jinja2 to parse through files looking for {{}},
# replace variables with real values, and send a complete HTML file back to the client.

# Jinja Documentation: https://jinja.palletsprojects.com/en/master/templates/

# Two different inputs in the HTML rendered will allow for python-like code in flask
{{ variable }}
{% expression %}

# Example server.py file:
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html", phrase="hello", times=5)

# Corresponding index.html example:
# <html>
#     <head>
#       <title>My First Template</title>
#     </head>
#     <body>
#       <h3>My flask template with embedded Python-like code</h3>
#       <!-- this will output the value of our phrase variable -->
#       <p>Phrase: {{ phrase }}</p>
#       <!-- this will output the value of our times variable -->
#       <p>Times: {{ times }}</p>
#       <!-- here is an example of embedding a for-loop in our code -->
#       {% for x in range(0,times): %}
#       <p>{{ phrase }}</p>
#       {% endfor %}
#       <!-- here is an example of embedding an if statement in our code -->
#       {% if phrase == "hello" %}
#       <p>The phrase says hello</p>
#       {% endif %}
#     </body>
# </html>

# This can also be used to pass in lists or a list of dictionaries to Jinja

# Example 2 server.py file:
@app.route('/')
def index():
    people_info = ({'name' : 'Michael', 'age' : 35},
       {'name' : 'Jon', 'age' : 30 },
       {'name' : 'Brittany', 'age' : 25},
       {'name' : 'Kris', 'age' : 27})
    return render_template("index.html", random_numbers = [3,1,5,7,4], people = people_info)

# The index.html template then can iterate through the list like this:
# <h1>Random Numbers</h1>
# {% for number in random_numbers %}
#     <p>{{ number }}</p>
# {% endfor %}
# <h1>Students</h1>
# {% for student in students %}
#     <p>{{ student['name'] }} - {{ student['age'] }}</p>
# {% endfor %}

##########################

# Static Files (images, css, etc)

# Things to remember:

# All static content must go inside of the static folder

# The folder MUST be named static

# In order to reference the static content start at the relative path after static
# (static is from the root(also known as / or the same level as your server.py file
    # For example, if you have styles.css file in a directory called css in your static 
    # folder your href would read "href='css/styles.css'"

# Linking a css style sheet:
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/my_styles.css') }}">
# Linking a javascript file:
<script type="text/javascript" src="{{ url_for('static', filename='js/my_script.js') }}"></script>
# Linking an image:
<img src="{{ url_for('static', filename='img/my_img.png') }}">