import streamlit as st

def show_home():
    st.markdown('<h1 style = "text-align: center;">Phoenix Home Price Predictor Model</div>',
                unsafe_allow_html=True)

    st.image('house.jpg')

    st.caption('This model was created to calculated a predicted house price based on a set of input criteria. The app contains a map of the model data, a zipcode scatterplot of sales between November 2021 and January 2023, a statistics page by zipcode, pool and HOA, a correlation of features visual and lastly the calculator. The model data is limited to a maximum selling price of 500,000.')