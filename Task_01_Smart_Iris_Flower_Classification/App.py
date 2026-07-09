# Smart Iris Flower Classification & Analytics System
# Home Page
import streamlit as st
import pandas as pd
# Page Configuration
st.set_page_config(
    page_title="Smart Iris Flower Classification and Advanced Features",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded"
)
# Load CSS
def load_css():
    with open("style.css") as css:
        st.markdown(
            f"<style>{css.read()}</style>",
            unsafe_allow_html=True
        )
load_css()
# Sidebar
st.sidebar.title("🌸 Navigation")
st.sidebar.success("Use the pages below to explore the project.")
st.sidebar.markdown("---")
st.sidebar.markdown("""
### 📌 Project Modules
- 🏠 Home
- 📊 Analytics Dashboard
- 🤖 Model Comparison
- 🌸 Flower Predictor
- 📖 Project Information
""")
st.sidebar.markdown("---")
st.sidebar.info(
"""
### 👩‍💻 Project

Smart Iris Flower Classification & Analytics System

Developed using Machine Learning & Streamlit.
"""
)
# Header
st.markdown(   """
    <h1 style='text-align: center; font-size: 48px; font-weight: bold;'>
        🌸 Smart Iris Flower Classification
    </h1>
    """, unsafe_allow_html=True)
st.markdown("""
<div class='subtitle'>
Machine Learning • Data Visualization • Streamlit Dashboard
</div>
""", unsafe_allow_html=True)
st.markdown("---")
# Hero Section
left, right = st.columns([2,1])
with left:
    st.markdown("""
### 🌼 Welcome

This dashboard demonstrates a complete Machine Learning workflow
using the famous Iris Flower Dataset.

You can explore:

- 📊 Exploratory Data Analysis
- 📈 Data Visualization
- 🤖 Machine Learning Models
- 🏆 Model Evaluation
- 🌸 Flower Prediction
- 📋 Prediction History

Use the sidebar to navigate through the application.
""")
with right:
    st.info("🌸 Dataset Samples : 150")
    st.info("🌼 Species : 3")
    st.info("🤖 ML Models : 6")
    st.info("🏆 Best Accuracy : 100%")
st.markdown("---")
# Project Highlights
st.subheader("✨ Project Highlights")
c1, c2, c3 = st.columns(3)
with c1:
    st.success("✔ Exploratory Data Analysis")
    st.success("✔ Statistical Analysis")
    st.success("✔ Feature Engineering")
    st.success("✔ Correlation Analysis")
with c2:
    st.success("✔ Pairplots")
    st.success("✔ Heatmaps")
    st.success("✔ Feature Importance")
    st.success("✔ Model Evaluation")
with c3:
    st.success("✔ 6 ML Algorithms")
    st.success("✔ Prediction System")
    st.success("✔ Model Saving")
    st.success("✔ Prediction History")
st.markdown("---")
# Dashboard Metrics
st.subheader("📊 Dashboard Overview")
m1, m2, m3, m4 = st.columns(4)
m1.metric("Dataset Samples", "150")
m2.metric("Species", "3")
m3.metric("Features", "8")
m4.metric("ML Models", "6")
st.markdown("---")
# Workflow
st.subheader("🤖 Machine Learning Workflow")
workflow = [
"Load Dataset",
"Data Cleaning",
"EDA",
"Feature Engineering",
"Train-Test Split",
"Feature Scaling",
"Train ML Models",
"Evaluate Models",
"Prediction"
]
for step in workflow:
    st.checkbox(step, value=True, disabled=True)
st.markdown("---")
# Dataset Information
st.subheader("📁 Dataset Information")
dataset = pd.DataFrame({
"Feature":[
"Sepal Length",
"Sepal Width",
"Petal Length",
"Petal Width",
"Petal Area",
"Sepal Area",
"Petal/Sepal Ratio",
"Flower Size Index"
],
"Type":[
"Numeric",
"Numeric",
"Numeric",
"Numeric",
"Engineered",
"Engineered",
"Engineered",
"Engineered"
]
})
st.dataframe(dataset, use_container_width=True)
st.markdown("---")
# Species Information
st.subheader("🌼 Iris Species")
tab1, tab2, tab3 = st.tabs(
[
"Setosa",
"Versicolor",
"Virginica"
]
)
with tab1:
    st.write("🌸 Small petals")
    st.write("Easy to classify")
    st.write("Usually perfectly separated")
with tab2:
    st.write("🌸 Medium petals")
    st.write("Moderate flower size")
    st.write("Sometimes overlaps with Virginica")
with tab3:
    st.write("🌸 Largest petals")
    st.write("Largest flower among all species")
    st.write("Usually classified with high confidence")
st.markdown("---")
# Technologies
st.subheader("🛠 Technologies Used")
col1, col2, col3 = st.columns(3)
with col1:
    st.info("🐍 Python")
    st.info("🐼 Pandas")
    st.info("🔢 NumPy")
with col2:
    st.info("🤖 Scikit-Learn")
    st.info("📊 Matplotlib")
    st.info("🎨 Seaborn")
with col3:
    st.info("🌐 Streamlit")
    st.info("💾 Joblib")
    st.info("📈 Plotly")
st.markdown("---")
# About Project
with st.expander("📖 About this Project"):
    st.write("""
This project demonstrates an end-to-end Machine Learning workflow
for Iris Flower Classification.

The application includes:

- Dataset Analysis
- Advanced Data Visualization
- Feature Engineering
- Machine Learning
- Model Comparison
- Flower Prediction
- Interactive Dashboard

It is designed as a portfolio-ready Data Science project.
""")
# Footer
st.markdown("""
<div class='footer'>
Developed with ❤️ using Python • Streamlit • Scikit-Learn
</div>
""", unsafe_allow_html=True)