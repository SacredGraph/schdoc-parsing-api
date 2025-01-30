import os

from flask import Flask, request
from altium_schematic_parser.parse import parse

app = Flask(__name__)


@app.route("/", methods = ['POST'])
def hello_world():
    url = request.form['url']
    schematic = parse(url, "all-hierarchy")

    return schematic


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))