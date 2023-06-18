"""
https://phoenixnap.com/kb/install-flask
https://developers.google.com/maps/documentation 
"""
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world!'

