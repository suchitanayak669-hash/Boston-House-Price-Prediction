import streamlit as st

st.set_page_config(
    page_title="About Project",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 About Boston House Price Analytics")

st.write(
    "A Machine Learning project designed to explore housing data "
    "and predict median house values using a trained regression model."
)

st.divider()

st.subheader("📌 Project Overview")

st.write("""
This project demonstrates how Machine Learning can be used
to analyse housing-related features and estimate house values.

The application provides an interactive platform where users
can explore the dataset, understand feature relationships,
and generate house price predictions.
""")

st.divider()

st.subheader("🎯 Problem Statement")

st.write("""
Estimating house prices involves analysing multiple factors,
such as the number of rooms, property-related characteristics,
and neighbourhood information.

This project uses a supervised Machine Learning regression
approach to estimate the target variable MEDV.
""")

st.divider()

st.subheader("⚙️ Project Workflow")

st.markdown("""
1. **Data Collection:** Load the Boston Housing dataset.
2. **Data Cleaning:** Prepare the dataset for analysis.
3. **Exploratory Data Analysis:** Study distributions and relationships.
4. **Data Preprocessing:** Prepare features for model building.
5. **Model Training:** Train regression models.
6. **Model Evaluation:** Evaluate model performance.
7. **Deployment:** Create an interactive Streamlit application.
""")

st.divider()

st.subheader("🛠️ Technologies Used")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🐍 Python")
    st.write("Programming language")

    st.markdown("### 🧮 Pandas")
    st.write("Data manipulation")

with col2:
    st.markdown("### 🤖 Scikit-learn")
    st.write("Machine Learning")

    st.markdown("### 📊 Plotly")
    st.write("Interactive visualisations")

with col3:
    st.markdown("### 📈 NumPy")
    st.write("Numerical computing")

    st.markdown("### 🌐 Streamlit")
    st.write("Web application")

st.divider()

st.subheader("📂 Dataset Information")

col1, col2, col3 = st.columns(3)

col1.metric("Total Records", "265")
col2.metric("Total Columns", "12")
col3.metric("Target Variable", "MEDV")

st.write(
    "The cleaned dataset contains 265 records and 12 columns, "
    "including the target variable MEDV."
)

st.divider()

st.subheader("⚠️ Project Limitations")

st.write("""
- This project uses a historical Boston Housing dataset.
- Its predictions should not be treated as current real estate market prices.
- The dataset has known ethical and representational limitations.
- Predictions depend on the features and patterns learned during model training.
""")

st.divider()

st.subheader("👩‍💻 Project Information")

st.write("**Project:** Boston House Price Analytics")
st.write("**Domain:** Machine Learning")
st.write("**Learning Area:** Supervised Learning – Regression")
st.write("**Application:** Interactive Web Application")

st.divider()

st.caption(
    "Developed as an educational Machine Learning project."
)