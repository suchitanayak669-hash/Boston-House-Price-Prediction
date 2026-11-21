
import streamlit as st

st.set_page_config(
    page_title="Boston House Price Analytics",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
.stApp {
    background-color: #F7F9FC;
}

[data-testid="stSidebar"] {
    background-color: #0B2447;
}

[data-testid="stSidebar"] * {
    color: white;
}

h1, h2, h3 {
    color: #0B2447;
}

div[data-testid="stMetric"] {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #E5EAF2;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("🏠 Boston Analytics")
st.sidebar.caption("House Price Prediction Platform")

st.title("Boston House Price Analytics")

st.write(
    "An interactive machine learning platform "
    "for house price prediction and data analysis."
)

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Project", "House Price Prediction")

with col2:
    st.metric("ML Approach", "Supervised Learning")

with col3:
    st.metric("Platform", "Streamlit")

st.divider()

st.subheader("Welcome to the Platform")

st.write(
    "Explore house price predictions, machine learning "
    "model performance, dataset analysis and insights."
)

st.info("Use the sidebar to navigate through the project.")

st.subheader("Project Features")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 🏡 Price Prediction

    Predict house prices using a trained ML model.

    ### 📊 Model Comparison

    Compare machine learning algorithms.
    """)

with col2:
    st.markdown("""
    ### 📈 EDA Dashboard

    Explore distributions and correlations.

    ### 🗂️ Dataset Explorer

    Explore the cleaned Boston dataset.
    """)
