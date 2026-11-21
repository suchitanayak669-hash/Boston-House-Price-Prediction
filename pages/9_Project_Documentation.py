
import streamlit as st

st.set_page_config(
    page_title="Project Documentation",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Project Documentation")

st.write(
    "Complete documentation of the Boston House Price Analytics project."
)

st.divider()

st.subheader("1. Project Introduction")

st.write("""
Boston House Price Analytics is a Machine Learning project
that uses housing-related features to estimate median house values.

The project combines data analysis, regression modelling,
and an interactive Streamlit application.
""")

st.divider()

st.subheader("2. Project Objectives")

st.markdown("""
- Explore and understand housing data.
- Perform exploratory data analysis.
- Apply Machine Learning regression techniques.
- Evaluate model performance.
- Build an interactive prediction application.
""")

st.divider()

st.subheader("3. Project Architecture")

st.code("""
Dataset
   |
   v
Data Cleaning
   |
   v
Exploratory Data Analysis
   |
   v
Data Preprocessing
   |
   v
Model Training
   |
   v
Model Evaluation
   |
   v
Saved ML Model (.pkl)
   |
   v
Streamlit Web Application
   |
   v
House Price Prediction
""", language="text")

st.divider()

st.subheader("4. Project Files")

st.markdown("""
| File | Purpose |
|---|---|
| app.py | Main application homepage |
| Boston_Cleaned_Data.csv | Cleaned dataset |
| boston_data.csv | Original dataset file |
| Boston_House_Price_Model.pkl | Saved trained model |
| requirements.txt | Python dependencies |
| BOSTON_EDA.ipynb | EDA notebook |
| Boston_model_build.ipynb | Model building notebook |
| prediction.ipynb | Prediction notebook |
| pages/ | Additional Streamlit pages |
""")

st.divider()

st.subheader("5. Installation Instructions")

st.write("Install the required Python packages:")

st.code(
    "python -m pip install -r requirements.txt",
    language="powershell"
)

st.write("Run the Streamlit application:")

st.code(
    "python -m streamlit run app.py",
    language="powershell"
)

st.divider()

st.subheader("6. Machine Learning Approach")

st.write("""
This project follows a supervised learning regression approach.

The input features are used by a trained regression model
to estimate the target variable MEDV.
""")

st.divider()

st.subheader("7. Important Disclaimer")

st.warning("""
This project uses a historical Boston Housing dataset.
Its predictions are intended for educational and demonstration
purposes only. They should not be used as current real estate
market valuations or financial advice.
""")

st.divider()

st.subheader("8. Future Improvements")

st.markdown("""
- Use more recent and representative housing data.
- Improve model evaluation and validation.
- Add additional regression algorithms.
- Improve the user interface.
- Deploy the application online.
""")

st.divider()

st.subheader("Project Summary")

st.success(
    "Boston House Price Analytics – "
    "A Machine Learning and Streamlit project."
)

st.caption("Project Documentation")
