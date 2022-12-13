import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk
import datetime
import pickle



def load_data():
    with open('data.pkl', 'rb') as f:
        data = pickle.load(f)
    return data
data = load_data()
data['ZIPCODE'] = data['ZIPCODE'].apply(np.int64)

def show_page3():
    subset_data = data
    metrics = ['BEDS','BATHS','SQFT','LOTSIZE','YEARBUILT','POOL','HOA']
    cols = st.selectbox('House Features to view', metrics)

    if cols in metrics:
           metrics_to_show = cols

    st.markdown('<h4 style = "text-align: center;">Choose features to view median prices for houses sold</div>',
                unsafe_allow_html=True)

 #ZIPCODE using multiselect streamlit tool
    features_input = st.multiselect(cols,data.groupby(metrics).count().reset_index()[[cols]].tolist())

    if len(features_input)>0:
        subset_data = data[data[[cols]].isin(features_input)]

    st.markdown('<h4 style = "text-align: center;">Median Phoenix Home Prices by Zipcode for previous 12 months</div>',
                unsafe_allow_html=True)

    prices_graph_by_metric = alt.Chart(subset_data).mark_line().encode(
        x=alt.X('SOLDDATE',  title='Sold Date'),
        y=alt.Y('median(PRICE):Q', title='Price'),
        #color = 'ZIPCODE:N',
    ).properties(
        width = 800,
        height = 600
    ).configure_axis(
        labelFontSize = 15,
        titleFontSize = 18
    )
    st.altair_chart(prices_graph_by_metric)




