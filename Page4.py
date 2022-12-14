import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sn
import pickle



def load_data():
    with open('modeldata.pkl', 'rb') as f:
        modeldata = pickle.load(f)
    return modeldata
model_data = load_data()

def show_page4():

    fig, ax=plt.subplots()
    sn.heatmap(data = model_data.corr(),ax=ax)
    st.write(fig)