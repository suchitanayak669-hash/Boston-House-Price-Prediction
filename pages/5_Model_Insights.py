
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Model Insights",
    page_icon="💡",
    layout="wide"
)

st.title("💡 Model Insights & Feature Analysis")
st.write("Explore the relationship between input features and house prices.")

st.divider()

# Load Dataset
df = pd.read_csv("Boston_Cleaned_Data.csv")

# Correlation Analysis
st.subheader("1. Feature Correlation with House Price")

correlation = df.select_dtypes(include="number").corr()

target_correlation = correlation["medv"].drop("medv")
target_correlation = target_correlation.sort_values(
    key=abs,
    ascending=False
)

correlation_df = target_correlation.reset_index()
correlation_df.columns = ["Feature", "Correlation"]

fig1 = px.bar(
    correlation_df,
    x="Feature",
    y="Correlation",
    color="Correlation",
    color_continuous_scale="RdBu",
    title="Correlation of Features with MEDV"
)

st.plotly_chart(fig1, use_container_width=True)

st.caption(
    "Correlation indicates the strength and direction of a linear relationship. "
    "It does not represent actual trained-model feature importance."
)

st.divider()

# Strongest Relationships
st.subheader("2. Strongest Feature Relationships")

top_features = target_correlation.head(5)

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Strongest Relationships")
    st.dataframe(
        top_features.rename("Correlation").to_frame(),
        use_container_width=True
    )

with col2:
    st.markdown("### Correlation Summary")
    st.metric(
        "Most Related Feature",
        target_correlation.index[0]
    )
    st.metric(
        "Correlation Value",
        f"{target_correlation.iloc[0]:.3f}"
    )

st.divider()

# Feature Relationship Explorer
st.subheader("3. Explore Feature Relationships")

selected_feature = st.selectbox(
    "Select a feature",
    [col for col in df.select_dtypes(include="number").columns
     if col != "medv"]
)

fig2 = px.scatter(
    df,
    x=selected_feature,
    y="medv",
    trendline="ols",
    title=f"{selected_feature} vs House Price (MEDV)",
    labels={
        "medv": "Median House Value",
        selected_feature: selected_feature
    }
)

st.plotly_chart(fig2, use_container_width=True)

st.divider()

# Full Correlation Matrix
st.subheader("4. Complete Correlation Matrix")

fig3 = px.imshow(
    correlation,
    text_auto=".2f",
    aspect="auto",
    color_continuous_scale="RdBu_r",
    title="Correlation Heatmap"
)

st.plotly_chart(fig3, use_container_width=True)

st.success("Model Insights page loaded successfully!")
