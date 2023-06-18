"""
https://phoenixnap.com/kb/install-flask
https://developers.google.com/maps/documentation

Will be used for drawing the path.
https://developers.google.com/maps/documentation/maps-static/start#Paths
"""
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world!'

