import os
from flask import Flask, request, jsonify, render_template, redirect
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


def process_input(data):

    # add empty keys for dummy-encoded property areas
    data['Property_Area_Urban'] = 0
    data['Property_Area_Semiurban'] = 0
    data['Property_Area_Rural'] = 0

    # convert to dataframe for easy processing
    df = pd.DataFrame([data])

    # create mapping dictionaries
    gender_values = {'Female': 0, 'Male': 1}
    married_values = {'No': 0, 'Yes': 1}
    education_values = {'Graduate': 0, 'Not Graduate': 1}
    employed_values = {'No': 0, 'Yes': 1}
    credit_history = {'No': 0, 'Yes': 1}
    dependent_values = {'3+': 3, '0': 0, '2': 2, '1': 1}

    # perform mapping of values
    df.replace({'Gender': gender_values, 'Married': married_values, 'Education': education_values,
                'Self_Employed': employed_values, 'Dependents': dependent_values, 'Credit_History': credit_history}, inplace=True)

    # map the property area to the appropriate encoded column
    propArea = df['Property_Area']
    df['Property_Area'+'_'+propArea] = 1

    # drop the property_area field
    df = df.drop('Property_Area', axis=1)

    return df

# Result route
@app.route('/approved')
def approved():
    return 'Congrats!'

# Result route
@app.route('/denied')
def denied():
    return 'Sorry!'

# Define home route
@app.route('/', methods=['GET', 'POST'])
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
                       'DAYS_EMPLOYED', 'FLAG_MOBIL', 'FLAG_WORK_PHONE', 'CNT_FAM_MEMBERS', 'LATEST_PAYMENT']
        #
        input_ary = [int(input_data[each_column])
                     if each_column in input_data else 0 for each_column in column_list]
        # input_ary=[0, 1, ...etc]
        print(input_ary)
        result = model.predict([input_ary])
        if result[0] == 'YES':
            return redirect('/approved')
        else:
            return redirect('/denied')
        # return render_template('index.html', TEST=result[0])  # , result=value)

    return render_template('index.html')


if __name__ == "__main__":
    # load_model()
    app.run(debug=True)
