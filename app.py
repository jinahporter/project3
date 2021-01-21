import os
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import numpy as np

# Define application
app = Flask(__name__)

# Load the saved model


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
        print(input_data)
        # Preprocess data
        #data = process_input(input_data)
        # Model prediction
        #value = model.predict(data)
        return render_template('index.html')  # , result=value)

    return render_template('index.html')


if __name__ == "__main__":
    load_model()
    app.run(debug=True)
