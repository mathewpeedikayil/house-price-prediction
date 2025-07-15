import streamlit as st
import pandas as pd

df = pd.read_csv("data.csv")

# ['area', 'bedrooms', 'bathrooms', 'stories', 'parking']
area_min = df["area"].min()
bedrooms_min = df["bedrooms"].min()
bathrooms_min = df["bathrooms"].min()
stories_min = df["stories"].min()
parking_min = df["parking"].min()

area_max = df["area"].max()
bedrooms_max = df["bedrooms"].max()
bathrooms_max = df["bathrooms"].max()
stories_max = df["stories"].max()
parking_max = df["parking"].max()

st.title("House Price Prediction 🏠")

area_sldr = st.slider("Area (sq ft)", area_min, area_max, 0)
bedrooms_sldr = st.slider("Number of bedrooms", bedrooms_min, bedrooms_max, 0)
bathrooms_sldr = st.slider("Number of bathrooms", bathrooms_min, bathrooms_max, 0)
stories_sldr = st.slider("Number of stories", stories_min, stories_max, 0)
parking_sldr = st.slider("Number of parking spaces", parking_min, parking_max, 0)


# streamlit run app.py

# References

# Finding Minimum and Maximum Values in a DataFrame Column
# https://discovery.cs.illinois.edu/guides/DataFrame-Row-Selection/finding-min-and-max/

# st.slider
# https://docs.streamlit.io/develop/api-reference/widgets/st.slider