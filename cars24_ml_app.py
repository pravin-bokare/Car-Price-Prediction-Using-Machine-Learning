import pandas as pd
import numpy as np
import datetime
import pickle
import streamlit as st
import sklearn

cars_df = pd.read_csv('cars24-car-price.csv')

st.write('''# Car Price Predictor''')
#st.dataframe(cars_df.head())

encode_dict = {
    'fuel_type':{'Diesel':1, 'Petrol':2, 'CNG':3, 'LPG':4, 'Electric':5},
    'seller_type':{'Dealer':1, 'Individual':2, 'Trustmark Dealer':3},
    'transmission_type':{'Manual':1, 'Automatic':2}
}

def model_pred(fuel_type, transmission_type, engine, seats, seller_type, mileage):
    with open('F:\iNeuron\ML Projects\Car Price Predictor Using Streamlit\car_pred.pkl', 'rb') as file:
        reg_model = pickle.load(file)
    input_features = [[fuel_type, transmission_type, engine, seats, seller_type, mileage]]
    return (reg_model.predict(input_features))




col1, col2, col3 = st.columns(3)

fuel_type = col1.selectbox('Select Fuel Type',
                         ['Diesel', 'Petrol', 'CNG', 'LPG', 'Electric'])

engine = col1.slider('Set the Engine Power',
                     500,5000,100)

transmission_type = col2.selectbox('Select Transmission Type',
                                   ['Manual', 'Automatic'])

seats = col2.selectbox('Select No. of Seats',
                       [4,5,6,7])

seller_type = col3.selectbox('Select the Seller Type',
                           ['Dealer', 'Individual', 'Trustmark Dealer'])

mileage = col3.slider('Select Mileage',
                      0, 120)

if st.button('Predict Price'):
    fuel_type = encode_dict['fuel_type'][fuel_type]
    transmission_type = encode_dict['transmission_type'][transmission_type]
    seller_type = encode_dict['seller_type'][seller_type]

    price = model_pred(fuel_type, transmission_type, engine, seats, seller_type, mileage)

    st.text('Predicted Price of the car : '+str(price))