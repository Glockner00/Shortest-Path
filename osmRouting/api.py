"""
https://phoenixnap.com/kb/install-flask
https://developers.google.com/maps/documentation

Will be used for drawing the path.
https://developers.google.com/maps/documentation/maps-static/start#Paths
"""
from flask import Flask, jsonify, request
import help

app = Flask(__name__)

@app.route('/generate_map_url', methods=['GET'])
def generate_map_url():
    start = (59.3116403, 14.4823716)
    end = (59.3067734, 14.4666375)
    p = help.get_urlpath_parameter(start, end)
    API_key = ""
    map_url = f"http://maps.googleapis.com/maps/api/staticmap?size=400x400&key={API_key}&path={p}"
    map_url = "https://www.google.com/maps/@59.3343444,14.5318915,12z?entry=ttu"

    return jsonify({'map_url': map_url})

if __name__ == '__main__':
    app.run()
