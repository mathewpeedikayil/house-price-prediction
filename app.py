import streamlit as st
import pandas as pd
import joblib

df = pd.read_csv("data.csv")
# ['area', 'bedrooms', 'bathrooms', 'stories', 'parking']

bedrooms_min = df["bedrooms"].min()
bathrooms_min = df["bathrooms"].min()
stories_min = df["stories"].min()
parking_min = df["parking"].min()

bedrooms_max = df["bedrooms"].max()
bathrooms_max = df["bathrooms"].max()
stories_max = df["stories"].max()
parking_max = df["parking"].max()

st.set_page_config(page_title="Dashboard")
st.title("House Price Prediction 🏠")

area_num_inpt = st.number_input("Area (sq ft)")
bedrooms_sldr = st.slider("Number of bedrooms", bedrooms_min, bedrooms_max, 0)
bathrooms_sldr = st.slider("Number of bathrooms", bathrooms_min, bathrooms_max, 0)
stories_sldr = st.slider("Number of stories", stories_min, stories_max, 0)
parking_sldr = st.slider("Number of parking spaces", parking_min, parking_max, 0)

# Sample Input
# 7420, 4, 2, 3, 2
input_data = pd.DataFrame([{
    'area': area_num_inpt,
    'bedrooms': bedrooms_sldr,
    'bathrooms': bathrooms_sldr,
    'stories': stories_sldr,
    'parking': parking_sldr
}])

lm = joblib.load('model.pkl')
if st.button("Predict House Price"):
    predicted_price = lm.predict(input_data)
    st.success(f"💰 Predicted House Price: $ {predicted_price[0]:,.0f}")

# streamlit run app.py

# References

# Finding Minimum and Maximum Values in a DataFrame Column
# https://discovery.cs.illinois.edu/guides/DataFrame-Row-Selection/finding-min-and-max/

# Input widgets
# https://docs.streamlit.io/develop/api-reference/widgets

# How to Save and Load Machine Learning Models in Python Using Joblib Library?
# https://www.analyticsvidhya.com/blog/2023/02/how-to-save-and-load-machine-learning-models-in-python-using-joblib-library/

# Force Reload of Webpage
# https://discuss.streamlit.io/t/force-reload-of-webpage/43793

# How to Deploy Your App to Streamlit Community Cloud
# https://www.youtube.com/watch?v=HKoOBiAaHGg