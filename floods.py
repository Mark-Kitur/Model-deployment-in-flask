from flask import Flask,jsonify, render_template, request, url_for
from joblib import load
import numpy as np
import pandas as pd
app =Flask(__name__, template_folder='templete')

model =load('floods.joblib')


@app.route('/')
def home():
    return render_template('floods.html')
@app.route('/', methods=['GET',"POST"])


def predict():
    if request.method == "POST":
        features = [float(x) for x in request.form.values()]
        array_features = [np.array(features)]
        prediction= model.predict(array_features)
    

        return render_template('floods.html', prediction=prediction)
    
    return render_template('floods.html')
if __name__ == '__main__':
    app.run(debug=True)