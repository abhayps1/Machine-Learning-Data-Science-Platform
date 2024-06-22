# Controller Layer

import os
from flask import Flask, request,jsonify

from connection_management import fetch_data
from service import get_description_stats

app = Flask(__name__)

# @app.route("/", methods=['POST'])
# def default_route():
#     payload = request.get_json()
#     from connection_management import fetch_data
#     return "This works"

@app.route("/get_desciptive_stats", methods=["GET"])
def get_quick_stats():
    columns = request.args.getlist("columns")
    connection_details = request.json
    df = fetch_data(connection_details)
    print("hell1 cols ", len(columns))
    print("hell1 cols ", columns)
    cols = jsonify(columns)
    print("hell2 cols ", cols)
    # get_description_stats(df, columns)
    return ""

if __name__ == "__main__":
    app.run(port=8080, debug=True)