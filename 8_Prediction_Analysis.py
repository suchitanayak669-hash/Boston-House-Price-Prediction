
import streamlit as st
import pandas as pd
import plotly.express as px
import pickle

st.set_page_config(
    page_title="Prediction Analysis",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Prediction Analysis")
st.write("Compare actual house prices with model predictions.")

st.divider()

# Load dataset and model
df = pd.read_csv("Boston_Cleaned_Data.csv")

with open("Boston_House_Price_Model.pkl", "rb") as file:
    model = pickle.load(file)

# Prepare input features
X = df.drop(columns=["medv"])

# Generate predictions
df["Predicted_MEDV"] = model.predict(X)

# Actual and predicted values
df["Actual_MEDV"] = df["medv"]

st.subheader("📊 Prediction Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Total Records", len(df))
col2.metric("Mean Actual MEDV", f'{df["Actual_MEDV"].mean():.2f}')
col3.metric("Mean Predicted MEDV", f'{df["Predicted_MEDV"].mean():.2f}')

st.divider()

# Actual vs Predicted
st.subheader("1. Actual vs Predicted House Prices")

fig1 = px.scatter(
    df,
    x="Actual_MEDV",
    y="Predicted_MEDV",
    title="Actual vs Predicted Values",
    labels={
        "Actual_MEDV": "Actual MEDV",
        "Predicted_MEDV": "Predicted MEDV"
    },
    hover_data=["ID"]
)

st.plotly_chart(fig1, use_container_width=True)

st.caption(
    "Points closer to the diagonal relationship indicate closer "
    "agreement between actual and predicted values."
)

st.divider()

# Prediction error
df["Prediction_Error"] = (
    df["Actual_MEDV"] - df["Predicted_MEDV"]
)

st.subheader("2. Prediction Error Distribution")

fig2 = px.histogram(
    df,
    x="Prediction_Error",
    nbins=30,
    title="Distribution of Prediction Errors"
)

st.plotly_chart(fig2, use_container_width=True)

st.divider()

# Prediction table
st.subheader("3. Actual and Predicted Values")

st.dataframe(
    df[[
        "ID",
        "Actual_MEDV",
        "Predicted_MEDV",
        "Prediction_Error"
    ]].round(2),
    use_container_width=True,
    hide_index=True
)

# Download results
csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    "⬇️ Download Prediction Results",
    data=csv,
    file_name="Boston_Prediction_Results.csv",
    mime="text/csv"
)
