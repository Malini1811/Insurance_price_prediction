import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Render the registration prediction form
@app.route('/')
def insurance():
    return render_template('insurance.html')

# Render the insurance information form
@app.route('/insurancepred')
def insurancepred():
    return render_template('insurancepred.html')
@app.route('/descrption')
def descrption():
    return render_template('descrption.html')

@app.route('/reg_pred')
def reg_pred():
    # Render the template and pass any necessary context
    return render_template('reg_pred.html')
@app.route('/remdie')
def remdie():
    return render_template('remdie.html')
@app.route('/thanku')
def thanku():
    return render_template('thanku.html')





# prediction function
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 8)
    loaded_model = pickle.load(open("regression.pickle", "rb"))
    result = loaded_model.predict(to_predict)
    return result[0]

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        result = ValuePredictor(to_predict_list)
        return render_template("reg_pred.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)
