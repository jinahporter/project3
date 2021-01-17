import os
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)


# create route that renders index.html template
@app.route("/")
def index():

    return render_template("index.html", TEST="testing")


if __name__ == "__main__":
    app.run(debug=True)
