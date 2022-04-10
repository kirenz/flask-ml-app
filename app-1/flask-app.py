from flask import Flask

# Creates an instance of the Flask class. 
# __name__ is a variable that represents the name of the application’s module
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
if __name__ == "__main__":
    app.run()