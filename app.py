import os
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)


@app.route("/")
def load_model():
    global model
    with open('LF_model.pkl', 'rb') as f:
        model = pickle.load(f)
        print("model loaded")

    return render_template("index.html", TEST="testing")


if __name__ == "__main__":
    app.run(debug=True)
