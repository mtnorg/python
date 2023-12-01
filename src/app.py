# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from flask import Flask
app = Flask(__name__)


@app.route("/")
def index() :
"""Module providing a function printing python version."""    
 
    return "Hello World"
if __name__=="__main__":
    app.run()
