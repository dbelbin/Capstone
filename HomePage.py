import streamlit as st

def show_home():
    st.markdown('<h1 style = "text-align: center;">Phoenix Home Price Predictor Model</div>',
                unsafe_allow_html=True)

    st.image('house.jpg')
