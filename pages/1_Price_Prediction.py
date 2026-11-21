
import streamlit as st
import pandas as pd
import pickle
from pathlib import Path

st.set_page_config(
    page_title="Price Prediction",
    page_icon="🏡",
    layout="wide"
)

st.title("🏡 House Price Prediction")
st.write("Enter the property details to generate a prediction.")

# Load Model
@st.cache_resource
def load_model():
    project_folder = Path(__file__).resolve().parent.parent

    model_path = (
        project_folder
        / "models"
        / "Boston_House_Price_Model.pkl"
    )

    with open(model_path, "rb") as file:
        return pickle.load(file)


model = load_model()

st.divider()

st.subheader("Property Details")

col1, col2 = st.columns(2)

with col1:
    ID = st.number_input("ID", min_value=1, value=25)
    indus = st.number_input("INDUS", value=7.07)
    chas = st.selectbox("CHAS", [0, 1])
    nox = st.number_input("NOX", value=0.469)
    rm = st.number_input("RM", value=6.421)
    age = st.number_input("AGE", value=78.9)

with col2:
    dis = st.number_input("DIS", value=4.967)
    rad = st.number_input("RAD", value=2)
    tax = st.number_input("TAX", value=242)
    ptratio = st.number_input("PTRATIO", value=17.8)
    lstat = st.number_input("LSTAT", value=9.14)

st.divider()

# Predict Button
if st.button(
    "🔮 Predict House Price",
    type="primary",
    use_container_width=True
):

    input_data = pd.DataFrame({
        "ID": [ID],
        "indus": [indus],
        "chas": [chas],
        "nox": [nox],
        "rm": [rm],
        "age": [age],
        "dis": [dis],
        "rad": [rad],
        "tax": [tax],
        "ptratio": [ptratio],
        "lstat": [lstat]
    })

    prediction = model.predict(input_data)

    st.success("Prediction generated successfully!")

    st.metric(
        label="Predicted MEDV",
        value=f"{prediction[0]:.2f}"
    )

    st.caption(
        "MEDV is expressed in thousands of US dollars in the "
        "original Boston Housing dataset. This is an educational "
        "model estimate, not a current market valuation."
    )
