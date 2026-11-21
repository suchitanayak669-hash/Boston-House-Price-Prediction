
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Model Comparison",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Machine Learning Model Comparison")
st.write("Compare the performance of different regression algorithms.")

st.divider()

# Model Performance Data
results = pd.DataFrame({
    "Model": [
        "Decision Tree",
        "Tuned Decision Tree",
        "KNN",
        "Tuned KNN",
        "Random Forest",
        "Tuned Random Forest"
    ],
    "MAE": [2.85, 2.72, 2.66, 2.40, 2.00, 2.11],
    "RMSE": [3.87, 3.86, 3.74, 3.12, 2.66, 2.75],
    "R2 Score": [0.387, 0.391, 0.483, 0.602, 0.692, 0.692]
})

st.subheader("Model Performance Table")

st.dataframe(
    results.style.format({
        "MAE": "{:.2f}",
        "RMSE": "{:.2f}",
        "R2 Score": "{:.3f}"
    }),
    use_container_width=True,
    hide_index=True
)

st.divider()

# Best Model
best_model = results.loc[results["RMSE"].idxmin()]

st.subheader("Best Performing Model")

col1, col2, col3 = st.columns(3)

col1.metric("Best Model", best_model["Model"])
col2.metric("Lowest RMSE", f"{best_model['RMSE']:.2f}")
col3.metric("R² Score", f"{best_model['R2 Score']:.3f}")

st.divider()

# RMSE Comparison
st.subheader("1. RMSE Comparison")

fig1 = px.bar(
    results,
    x="Model",
    y="RMSE",
    color="RMSE",
    title="Root Mean Squared Error Comparison",
    color_continuous_scale="Blues",
    text_auto=".2f"
)

st.plotly_chart(fig1, use_container_width=True)

st.caption("Lower RMSE indicates better prediction accuracy.")

st.divider()

# MAE Comparison
st.subheader("2. MAE Comparison")

fig2 = px.bar(
    results,
    x="Model",
    y="MAE",
    color="MAE",
    title="Mean Absolute Error Comparison",
    color_continuous_scale="Viridis",
    text_auto=".2f"
)

st.plotly_chart(fig2, use_container_width=True)

st.divider()

# R2 Comparison
st.subheader("3. R² Score Comparison")

fig3 = px.bar(
    results,
    x="Model",
    y="R2 Score",
    color="R2 Score",
    title="R² Score Comparison",
    color_continuous_scale="Teal",
    text_auto=".3f"
)

st.plotly_chart(fig3, use_container_width=True)

st.divider()

# Select Model
st.subheader("Explore Individual Models")

selected_model = st.selectbox(
    "Choose a Machine Learning Model",
    results["Model"]
)

model_details = results[
    results["Model"] == selected_model
].iloc[0]

st.write("### Selected Model:", selected_model)

col1, col2, col3 = st.columns(3)

col1.metric("MAE", f"{model_details['MAE']:.2f}")
col2.metric("RMSE", f"{model_details['RMSE']:.2f}")
col3.metric("R² Score", f"{model_details['R2 Score']:.3f}")

st.success("Model comparison dashboard loaded successfully!")
