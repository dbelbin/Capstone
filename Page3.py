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


data['POOL'] = np.where(data['POOL'] == 1,'Y','N')
data['HOA'] = np.where(data['HOA'] == 1,'Y','N')
data = data[['ZIPCODE','PRICE','BEDS','BATHS','SQFT','LOTSIZE','YEARBUILT','POOL','HOA']]
data['ZIPCODE']=data['ZIPCODE'].astype('int64')
data['YEARBUILT']=data['YEARBUILT'].astype('int64')
data['SQFT']=data['SQFT'].astype('int64')
data['LOTSIZE']=data['LOTSIZE'].astype('int64')
data['BEDS']=data['BEDS'].astype('int32')

def show_page3():
    st.markdown('<h2 style = "text-align: center;">Statistics of Home Sales</div>', unsafe_allow_html=True)

    st.header('Median statistics based on ZipCode, Pool and HOA')
    statistics = data.groupby(['ZIPCODE','POOL','HOA']).median('PRICE')
    #statistics = statistics.reset_index(inplace=True)
    statistics = statistics.rename_axis(index=['ZIPCODE','POOL','HOA'])
    st.dataframe(statistics)





