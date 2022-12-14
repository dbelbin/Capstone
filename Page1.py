import streamlit as st
import pandas as pd
import numpy as np
import pickle
import pydeck as pdk

def load_data():
    with open('data.pkl', 'rb') as f:
        data = pickle.load(f)
    return data

data = load_data()

df = data[['LATITUDE','LONGITUDE']]
df = df.rename(columns = {'LATITUDE':'lat'})
df = df.rename(columns = {'LONGITUDE':'lon'})

def show_page1():

    st.markdown('<h2 style = "text-align: center;">Map of Historical Home Sales</div>', unsafe_allow_html=True)

    st.markdown('<h3 style = "text-align: center;">Data points used to create the prediction model</div>', unsafe_allow_html=True)


    st.pydeck_chart(pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=33.44,
            longitude=-112.07,
            zoom=8.5,
            pitch=0,
        ),
        layers = [
            pdk.Layer(
                'ScatterplotLayer',
                data=df,
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                get_radius=200,
            ),
        ],
    ))
    st.markdown('<h6 style = "text-align: center;">Data points represent 1 year of sold houses below $500,000</div>',unsafe_allow_html=True)