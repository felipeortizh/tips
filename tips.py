


import streamlit as st


pio.renderers.default = "browser"

st.title("A Waiter's Tip Prediction")
st.header("""
This Web App predicts the tip given by a customer. 
""")

st.subheader("""
Machine Learning model = Multilinear Regression. 
""")


total_bill = st.sidebar.slider("Total bill (in dollars)", 1,300)
