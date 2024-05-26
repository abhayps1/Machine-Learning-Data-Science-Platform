# Controller Layer

import os
from flask import Flask, request,jsonify

app = Flask(__name__)

@app.route("/", methods=['POST'])
def default_route():
    payload = request.get_json()
    from connection_management import fetch_data
    fetch_data(payload)
    return "This works"


if __name__ == "__main__":
    app.run(port=8080, debug=True)