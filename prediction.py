import streamlit as st
import pickle
import pandas as pd
import numpy as np

def load_model():
   with open('trained_model.pkl', 'rb') as file:
    model = pickle.load(file)
    return model

model = load_model()

RF_loaded = model["model"]

with open('scaler.pkl', 'rb') as f:
    scaler=pickle.load(f)

def show_prediction():
    with st.form(key='my_form'):
        st.title("Phoenix home price calculator")
        st.write("""### Enter the following criteria to calculate predicted price""")
        ZIPCODE = ('85001','85002','85003','85004','85005','85006','85007','85008','85009','85010','85011','85012','85013','85014','85015','85016','85017','85018','85019','85020','85021','85022','85023','85024','85026','85027','85028','85029','85030','85031','85032','85033','85034','85035','85036','85037','85038','85039','85040','85041','85042','85043','85044','85045','85046','85048','85050','85051','85053','85054','85060','85061','85062','85063','85064','85065','85066','85067','85068','85069','85070','85071','85072','85073','85074','85075','85076','85078','85079','85080','85082','85083','85085','85086','85087')
        BEDS = (1,2,3,4,5)
        BATHS = (1, 1.5,2,2.5,3,3.5,4)
        POOL = ('Y','N')
        HOA = ('Y','N')


        ZIPCODE = st.selectbox("Select the ZipCode",ZIPCODE)
        BEDS = st.selectbox("Select the Number of Bedrooms", BEDS)
        BATHS = st.selectbox("Select the Number of Bathrooms",BATHS)
        SQFT = st.number_input ("Enter the Square Footage of House", min_value=500, max_value=3500, value=1500)
        LOTSIZE = st.number_input("Select Lot Size", min_value=3500,max_value=15000, value=7000)
        YEARBUILT = st.number_input("Enter the year the house was built", min_value = 1915, max_value=2023, value = 2015)
        POOL = st.checkbox("Pool", help("Check the box if the house has a pool"))
        HOA = st.checkbox("HOA", help("Check the box if the house is in an HOA"))

        submit_button = st.form_submit_button(label = 'Calculate Predicted Price')

    if submit_button:
        X=encoder.transform([[ZIPCODE,BEDS,BATHS,SQFT,LOTSIZE,YEARBUILT,POOL,HOA]])
        X = scaler.transform(X)

        prediction = RF_loaded.predict(X)
        st._show(prediction)





