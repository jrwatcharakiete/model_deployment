
from flask import Flask, request
import pandas as pd
import numpy as np
import pickle
import flasgger
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

pickle_in = open('rfc_banknoteauth.pkl', 'rb')
clf = pickle.load(pickle_in)

@app.route('/')
def welcome():
    return 'Welcome All'

@app.route('/predict')
def predict_bankauth():
    """
    ---
    parameters:
    -   name: variance
        in: query
        type: number
        required: true
    -   name: skewness
        in: query
        type: number
        required: true
    -   name: curtosis
        in: query
        type: number
        required: true
    -   name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
    """

    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    prediction = clf.predict([[variance, skewness, curtosis, entropy]])
    return 'The prediction is {}'.format(prediction)

@app.route('/predict_file', methods=['POST'])
def predict_bankauth_file():
    """
        ---
        parameters:
        -   name: file
            in: formData
            type: file
            required: true
        responses:
            200:
                description: The output values
        """

    df = pd.read_csv(request.files.get('file'))
    prediction = clf.predict(df)
    return 'The prediction is {}'.format(list(prediction))

if __name__ == '__main__':
    app.run()
