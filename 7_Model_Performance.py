
import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(
    page_title="Model Performance",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Model Performance Dashboard")

st.write(
    "Compare regression model performance using evaluation metrics."
)

st.divider()

st.subheader("📌 Evaluation Metrics")

st.write("""
Upload a CSV file containing the evaluation results from your
model-building notebook.

Required columns:
- Model
- MAE
- MSE
- RMSE
- R2 Score
""")

uploaded_file = st.file_uploader(
    "Upload your model comparison CSV",
    type=["csv"]
)

if uploaded_file is not None:

    results = pd.read_csv(uploaded_file)

    required_columns = [
        "Model", "MAE", "MSE", "RMSE", "R2 Score"
    ]

    if all(column in results.columns for column in required_columns):

        st.success("Model results loaded successfully!")

        st.subheader("Model Comparison Table")

        st.dataframe(
            results,
            use_container_width=True,
            hide_index=True
        )

        st.divider()

        st.subheader("Performance Metrics")

        col1, col2, col3 = st.columns(3)

        best_rmse = results.loc[results["RMSE"].idxmin()]
        best_mae = results.loc[results["MAE"].idxmin()]
        best_r2 = results.loc[results["R2 Score"].idxmax()]

        col1.metric("Lowest RMSE", f'{best_rmse["RMSE"]:.3f}')
        col2.metric("Lowest MAE", f'{best_mae["MAE"]:.3f}')
        col3.metric("Highest R²", f'{best_r2["R2 Score"]:.3f}')

        st.divider()

        st.subheader("RMSE Comparison")

        fig1 = px.bar(
            results,
            x="Model",
            y="RMSE",
            color="RMSE",
            title="RMSE Comparison (Lower is Better)",
            color_continuous_scale="Blues"
        )

        st.plotly_chart(fig1, use_container_width=True)

        st.subheader("MAE Comparison")

        fig2 = px.bar(
            results,
            x="Model",
            y="MAE",
            color="MAE",
            title="MAE Comparison (Lower is Better)",
            color_continuous_scale="Viridis"
        )

        st.plotly_chart(fig2, use_container_width=True)

        st.subheader("R² Score Comparison")

        fig3 = px.bar(
            results,
            x="Model",
            y="R2 Score",
            color="R2 Score",
            title="R² Score Comparison (Higher is Better)",
            color_continuous_scale="Teal"
        )

        st.plotly_chart(fig3, use_container_width=True)

        st.divider()

        st.subheader("🏆 Best Models")

        st.write("**Best RMSE:**", best_rmse["Model"])
        st.write("**Best MAE:**", best_mae["Model"])
        st.write("**Best R² Score:**", best_r2["Model"])

    else:
        st.error(
            "Your CSV must contain these columns: "
            "Model, MAE, MSE, RMSE, R2 Score"
        )

else:
    st.info(
        "Upload your model evaluation CSV to view the dashboard. "
        "No sample or assumed performance values are displayed."
    )

