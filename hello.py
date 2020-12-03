# Example "Hello World" server

# For flask 1.0.2

# Do not run in app, run with:
# FLASK_APP=hello.py flask run

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!" 

# Additional example routes:

@app.route('/success')
def success():
  return "success"

@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "hello "+name

@app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id
