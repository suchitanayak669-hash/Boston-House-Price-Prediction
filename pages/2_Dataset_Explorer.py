import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dataset Explorer",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Boston Housing Dataset Explorer")
st.write("Explore, search and analyse the Boston Housing dataset.")

st.divider()

df = pd.read_csv("Boston_Cleaned_Data.csv")

st.subheader("Dataset Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Records", df.shape[0])

with col2:
    st.metric("Total Columns", df.shape[1])

with col3:
    st.metric("Missing Values", int(df.isnull().sum().sum()))

st.divider()

st.subheader("Dataset Preview")

search = st.text_input("🔍 Search dataset")

if search:
    filtered_df = df[
        df.astype(str).apply(
            lambda column: column.str.contains(
                search, case=False, na=False
            )
        ).any(axis=1)
    ]
else:
    filtered_df = df

st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True
)

st.write(f"Showing {len(filtered_df)} records")

st.divider()

st.subheader("Statistical Summary")

st.dataframe(
    df.describe().round(2),
    use_container_width=True
)

st.divider()

st.subheader("Dataset Information")

selected_column = st.selectbox(
    "Select a column",
    df.columns
)

st.write("Column:", selected_column)
st.write("Data Type:", str(df[selected_column].dtype))
st.write("Unique Values:", int(df[selected_column].nunique()))
st.write("Missing Values:", int(df[selected_column].isnull().sum()))

st.divider()

st.subheader("Download Dataset")

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇️ Download Cleaned Dataset",
    data=csv,
    file_name="Boston_Cleaned_Data.csv",
    mime="text/csv"
)