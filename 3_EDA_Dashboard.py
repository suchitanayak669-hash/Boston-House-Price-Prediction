import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="EDA Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Exploratory Data Analysis")
st.write("Interactive analysis of the Boston Housing Dataset.")

df = pd.read_csv("Boston_Cleaned_Data.csv")

st.divider()

# Dataset Overview
st.subheader("Dataset Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Total Records", df.shape[0])
col2.metric("Total Features", df.shape[1] - 1)
col3.metric("Missing Values", int(df.isnull().sum().sum()))

st.divider()

# MEDV Distribution
st.subheader("1. House Price Distribution")

fig1 = px.histogram(
    df,
    x="medv",
    nbins=30,
    title="Distribution of House Prices",
    color_discrete_sequence=["#576CBC"]
)

st.plotly_chart(fig1, use_container_width=True)

st.divider()

# RM vs MEDV
st.subheader("2. Number of Rooms vs House Price")

fig2 = px.scatter(
    df,
    x="rm",
    y="medv",
    title="Rooms vs House Price",
    color="medv",
    color_continuous_scale="Blues",
    labels={
        "rm": "Average Number of Rooms",
        "medv": "Median House Value"
    }
)

st.plotly_chart(fig2, use_container_width=True)

st.divider()

# LSTAT vs MEDV
st.subheader("3. LSTAT vs House Price")

fig3 = px.scatter(
    df,
    x="lstat",
    y="medv",
    title="LSTAT vs House Price",
    color="medv",
    color_continuous_scale="Viridis"
)

st.plotly_chart(fig3, use_container_width=True)

st.divider()

# Correlation Heatmap
st.subheader("4. Correlation Heatmap")

correlation = df.select_dtypes(include="number").corr()

fig4 = px.imshow(
    correlation,
    text_auto=".2f",
    aspect="auto",
    color_continuous_scale="RdBu_r",
    title="Feature Correlation Matrix"
)

st.plotly_chart(fig4, use_container_width=True)

st.divider()

# Feature Distribution
st.subheader("5. Feature Distribution")

selected_feature = st.selectbox(
    "Select a feature",
    df.select_dtypes(include="number").columns
)

fig5 = px.histogram(
    df,
    x=selected_feature,
    marginal="box",
    title=f"Distribution of {selected_feature}",
    color_discrete_sequence=["#19376D"]
)

st.plotly_chart(fig5, use_container_width=True)

st.success("EDA Dashboard loaded successfully!")
