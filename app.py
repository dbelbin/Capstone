import streamlit as st

from HomePage import show_home
from Page1 import show_page1
from Page2 import show_page2
from Page3 import show_page3
from Page4 import show_page4
from prediction import show_prediction

st.sidebar.image('Sold.png', width=150)
page = st.sidebar.title("Pages")
page = st.sidebar.selectbox("Data Exploration or Prediction",("Home","Map of Historical Home Sales","Historical Prices by Zip Code","Statistics","Correlation of Features", "Calculator"))

if page == "Home":
    show_home()
elif page == "Map of Historical Home Sales":
    show_page1()
elif page == "Historical Prices by Zip Code":
    show_page2()
elif page == "Statistics":
    show_page3()
elif page == "Correlation of Features":
    show_page4()
else:
    show_prediction()