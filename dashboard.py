import streamlit as st
import pandas as pd
import requests

st.title("Amazon Product Analytics Dashboard")

api_url = "http://127.0.0.1:5000/products"

response = requests.get(api_url)
data = response.json()

df = pd.DataFrame(data)

# show dataset
st.subheader("Dataset Preview")
st.dataframe(df)

# rating distribution
st.subheader("Rating Distribution")
st.bar_chart(df["rating"].value_counts())

# category distribution
st.subheader("Products per Category")
st.bar_chart(df["category"].value_counts())

# discount analysis
st.subheader("Discount Percentage Distribution")
st.bar_chart(df["discount_percentage"].value_counts())