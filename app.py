from flask import Flask, render_template,request
import sklearn

import numpy as np
import pickle

model= pickle.load(open('new_model.pkl','rb'))
app= Flask(__name__)

app= Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict_termdeposit():
    duration=float(request.form.get('duration'))
    Euribor_3M = float(request.form.get('Euribor_3M'))
    Cust_Conf_Index = float(request.form.get('Cust_Conf_Index'))
    Cust_Price_Index = float(request.form.get('Cust_Price_Index'))
    age = int(request.form.get('age'))
    month = int(request.form.get('month'))
    day_of_week = int(request.form.get('day_of_week'))
    campaign = int(request.form.get('campaign'))
    job = int(request.form.get('job'))
    default = int(request.form.get('default'))

    result=model.predict(np.array([duration,Euribor_3M,Cust_Conf_Index,Cust_Price_Index,age,month,day_of_week,campaign,job,default]).reshape(1,10))



    if result[0]==1:
        result='Subscribed Term Deposit'
    else:
        result = 'Did not subscribe Term Deposit'

    return str(result)

if __name__=='__main__':
    app.run(debug=True)
