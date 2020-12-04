# Example "Hello World" server

# For flask 1.0.2

# Do not run in app, run with:
# FLASK_APP=hello.py flask run

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html', name="Kristopher")

# Notes on Templates:
# Template should be in a "templates" directory in the same location as server.py

# Flask uses a templating engine called Jinja2 to parse through files looking for {{}},
# replace variables with real values, and send a complete HTML file back to the client.

# For older version of flask, run server in the file, different for 1.0.2+
# For 1.0.2+ see line 6 above
# if __name__=="__main__": 
#     app.run(debug=)True


############################
# Additional example routes:
############################

@app.route('/success')
def success():
  return "success"

# for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
@app.route('/hello/<name>')
def hello(name):
    print(name)
    return "hello "+name

# for a route '/users/____/____', two parameters in the url get passed as username and id
@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id
