import streamlit as st
import numpy as np
import altair as alt
import pickle

@st.cache
def load_data():
    with open('data.pkl', 'rb') as f:
        data = pickle.load(f)
    return data
data = load_data()
data['ZIPCODE'] = data['ZIPCODE'].apply(np.int64)

def show_page2():
    st.markdown('<h4 style = "text-align: center;">Choose one or more zipcodes to view median prices for houses sold</div>',
                unsafe_allow_html=True)
    subset_data = data
 #ZIPCODE using multiselect streamlit tool
    zipcode_input = st.multiselect('Zip Code',data.groupby('ZIPCODE').count().reset_index()['ZIPCODE'].tolist())

    if len(zipcode_input)>0:
        subset_data = data[data['ZIPCODE'].isin(zipcode_input)]

    st.markdown('<h4 style = "text-align: center;">Median Phoenix Home Prices by Zipcode for previous 12 months</div>',
                unsafe_allow_html=True)

    prices_graph = alt.Chart(subset_data).mark_line().encode(
        x=alt.X('SOLDDATE',  title='Sold Date'),
        y=alt.Y('median(PRICE):Q', title='Price'),
        color = 'ZIPCODE:N',
    ).properties(
        width = 800,
        height = 600
    ).configure_axis(
        labelFontSize = 15,
        titleFontSize = 18
    )
    st.altair_chart(prices_graph)

    st.write(subset_data)


