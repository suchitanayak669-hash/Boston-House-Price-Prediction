import streamlit as st

st.set_page_config(
    page_title="Boston House Price Analytics",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🏠 Boston House Price Analytics")

st.subheader("Welcome to Our Machine Learning Project")

st.write("""
Explore our interactive Boston House Price Prediction
platform, developed using Python, Machine Learning
and Streamlit.
""")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Project", "House Price Prediction")

with col2:
    st.metric("Technology", "Machine Learning")

with col3:
    st.metric("Framework", "Streamlit")

st.divider()

st.header("Explore Our Project")

st.write("""
Use the navigation sidebar to explore all nine sections
of our Boston House Price Prediction project.

You can explore the dataset, visualize relationships,
compare machine learning models and predict house prices.
""")

st.info(
    "Select any project page from the sidebar to get started."
)
