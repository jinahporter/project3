import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
import pickle
import pandas as pd
import numpy as np

# data_dict={'Male': 1, 'Female': 0}

# Define application
app = Flask(__name__)

# Load the saved model
with open('LF_model.pkl', 'rb') as f:
    model = pickle.load(f)


def load_model():
    global model
    with open('LF_model.pkl', 'rb') as f:
        model = pickle.load(f)
        print("model loaded")

# Result route
@app.route('/approved.html')
def approved():
    return render_template('approved.html')

# Result route
@app.route('/denied.html')
def denied():
    return render_template('denied.html')

# Credit info route
@app.route('/credit_interactive.html')
def credit_interactive():
    return render_template('credit_interactive.html')

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Define form submission route
@app.route('/form_submission.html', methods=['GET', 'POST'])
def index():
    # When user clicks submit
    if request.method == 'POST':
        # Dictionary of all fields from the html form ### use converted numerical values
        # CODE_GENDER = request.form.get("CODE_GENDER")
        # print(f"CODE_GENDER = {CODE_GENDER}")
        # FLAG_OWN_CAR = request.form.get("FLAG_OWN_CAR")
        # print(f"FLAG_OWN_CAR = {FLAG_OWN_CAR}")
        # CNT_CHILDREN = request.form.get("CNT_CHILDREN")
        # print(f"CNT_CHILDREN = {CNT_CHILDREN}")
        # NAME_EDUCATION_TYPE = request.form.get("NAME_EDUCATION_TYPE")
        # print(f"NAME_EDUCATION_TYPE = {NAME_EDUCATION_TYPE}")
        # NAME_FAMILY_STATUS = request.form.get("NAME_FAMILY_STATUS")
        # print(f"NAME_FAMILY_STATUS = {NAME_FAMILY_STATUS}")

        input_data = request.form.to_dict()
        for each_key in input_data:
            if input_data[each_key] == '':
                input_data[each_key] = 0
        # {'ID': 0, 'CODE_GENDER': 1, ...etc}
        print(input_data)
        # Preprocess data
        #data = process_input(input_data)
        # static_input = [0, 1, 1, 1, 0, 226, 4,
        #                 1, 0, 4, 5609, 1005, 0, 1, 1, 3]
        # Model prediction
        column_list = ['CODE_GENDER', 'FLAG_OWN_CAR', 'FLAG_OWN_REALTY', 'CNT_CHILDREN',
                       'AMT_INCOME_TOTAL', 'NAME_INCOME_TYPE', 'NAME_EDUCATION_TYPE',
                       'NAME_FAMILY_STATUS', 'NAME_HOUSING_TYPE', 'DAYS_BIRTH',
                       'DAYS_EMPLOYED', 'FLAG_MOBIL', 'FLAG_WORK_PHONE', 'CNT_FAM_MEMBERS', 'SUM']
        #
        input_ary = [int(input_data[each_column])
                     if each_column in input_data else 0 for each_column in column_list]
        # input_ary=[0, 1, ...etc]
        print(input_ary)
        result = model.predict([input_ary])
        print(f'decision {result[0]}')
        if result[0] == 1:
            return redirect('/approved.html')
        else:
            return redirect('/denied.html')

        # return render_template('index.html', TEST=result[0])  # , result=value)

    return render_template('form_submission.html')


if __name__ == "__main__":
    # load_model()
    app.run(debug=True)
