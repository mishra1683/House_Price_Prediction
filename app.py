import streamlit as st
import pandas as pd
import pickle
import numpy as np
st.markdown("<h1 style='text-align: center; color: red;'>House Price Predictor</h1>", unsafe_allow_html=True)
st.sidebar.write("Enter House Details")
m=pd.read_csv('USA_Housing.csv')
model=pickle.load(open('HousePredictionLinearRegressionModel.pkl','rb'))
def predict(a,b,c,d,e):
    p=model.predict(pd.DataFrame(columns=["Avg. Area Income","Avg. Area House Age","Avg. Area Number of Rooms","Avg. Area Number of Bedrooms","Area Population"],data=np.array([a,b,c,d,e]).reshape(1,5)))
    return st.write("The Reselling Price of House is",float(p))
A=st.sidebar.text_input("Avg. Area Income")
B=st.sidebar.text_input("Avg. Area House Age")
C=st.sidebar.text_input("Avg. Area Number of Rooms")
D=st.sidebar.text_input("Avg. Area Number of Bedrooms")
E=st.sidebar.text_input("Area Population")
if st.sidebar.button("Predict"):
    predict(A,B,C,D,E)