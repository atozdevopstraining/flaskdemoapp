# app.py
from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Use the route() decorator to bind a function to a URL
@app.route("/")
def hello_world():
    return "<p>Hello, World! This is a Flask demo.</p>"

# bind multiple URL for one view function
@app.route('/hi')
@app.route('/hello')
def say_hello():
    return '<h1>Hello, Flask!</h1>'


# dynamic route, URL variable default
@app.route('/greet', defaults={'name': 'Programmer'})
@app.route('/greet/<name>')
def greet(name):
    return '<h1>Hello, %s!</h1>' % name


# Optional: Run the application directly if the script is executed
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)

