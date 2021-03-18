# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 16:46:35 2021

@author: Riddhi Parmar
"""

from flask import Flask,request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)
pickle_in=open('classifier.pkl','rb')
classifier=pickle.load(pickle_in)   


@app.route('/')
def welcom():
    return "Welcome All"

@app.route('/predict')
def predict_note_authentication():
    variance=request.args.get('variance')
    skewness=request.args.get('skewness')
    curtosis=request.args.get('curtosis')
    entropy=request.args.get('entropy')
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    return "The Predicted Values Is"+ str(prediction) 

@app.route('/predict_file',methods=["POST"])
def predict_note_file():
    def_test=pd.read_csv(request.files.get("file"))
    prediction=classifier.predict(df_test)
    return "The Predicted Value For The Csv Is"+ str(list(prediction) )

if __name__=='__main__':
    app.run()
