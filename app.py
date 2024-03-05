from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root URL("/")
@app.route('/')
def index():
    return "<h1>Hello, welcome to my web app!</h1>"

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
