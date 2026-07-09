import streamlit as st
import pandas as pd
import os

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Project Information",
    page_icon="📘",
    layout="wide"
)

# ==========================================================
# LOAD CSS
# ==========================================================

css_path = "style.css"

if os.path.exists(css_path):
    with open(css_path) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# ==========================================================
# HEADER
# ==========================================================

st.markdown("""
<h1 style='text-align:center;color:#6C63FF;'>
📘 Smart Iris Flower Classification
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<div style='text-align:center;font-size:18px;'>
A Machine Learning based Streamlit Dashboard developed for
predicting Iris flower species using four flower measurements.
</div>
""", unsafe_allow_html=True)

st.divider()

# ==========================================================
# PROJECT OVERVIEW
# ==========================================================

st.header("📌 Project Overview")

st.write("""
The **Smart Iris Flower Classification Dashboard** is a Machine
Learning application built with Streamlit that predicts the
species of an Iris flower using its physical measurements.

The project combines data analysis, machine learning,
interactive visualization, and an intuitive web interface
into a single dashboard.

It demonstrates a complete Data Science workflow, starting
from dataset exploration to model prediction and result
interpretation.
""")

st.divider()

# ==========================================================
# PROJECT OBJECTIVES
# ==========================================================

st.header("🎯 Project Objectives")

col1, col2 = st.columns(2)

with col1:

    st.success("""
✔ Predict Iris flower species

✔ Interactive user interface

✔ Fast machine learning prediction

✔ Easy to understand dashboard

✔ Educational demonstration
""")

with col2:

    st.info("""
✔ Visualize dataset

✔ Compare prediction results

✔ Store prediction history

✔ Learn classification concepts

✔ Portfolio-ready project
""")

st.divider()

# ==========================================================
# DATASET INFORMATION
# ==========================================================

st.header("🌸 Iris Dataset")

col1, col2 = st.columns([1,2])

with col1:

    st.metric("Samples", "150")

    st.metric("Features", "4")

    st.metric("Classes", "3")

with col2:

    st.write("""
The Iris dataset is one of the most famous datasets in
Machine Learning.

It contains measurements from three different Iris flower
species:

• Iris Setosa

• Iris Versicolor

• Iris Virginica

Each flower contains four numerical measurements used
to train the machine learning model.
""")

st.divider()

# ==========================================================
# FEATURES DESCRIPTION
# ==========================================================

st.header("📊 Input Features")

feature_df = pd.DataFrame({

    "Feature":[
        "Sepal Length",
        "Sepal Width",
        "Petal Length",
        "Petal Width"
    ],

    "Description":[
        "Length of Sepal (cm)",
        "Width of Sepal (cm)",
        "Length of Petal (cm)",
        "Width of Petal (cm)"
    ]

})

st.dataframe(
    feature_df,
    use_container_width=True
)

st.divider()

# ==========================================================
# TARGET CLASSES
# ==========================================================

st.header("🌼 Target Classes")

col1, col2, col3 = st.columns(3)

with col1:

    st.success("""
### 🌸 Setosa

• Small petals

• Easily separable

• High prediction accuracy
""")

with col2:

    st.warning("""
### 🌼 Versicolor

• Medium-sized flower

• Balanced characteristics

• Moderate petal size
""")

with col3:

    st.error("""
### 🌺 Virginica

• Largest petals

• Mature flower

• Higher petal width
""")

st.divider()

# ==========================================================
# MACHINE LEARNING WORKFLOW
# ==========================================================

st.header("🤖 Machine Learning Workflow")

workflow = [
    "Dataset Collection",
    "Data Cleaning",
    "Exploratory Data Analysis",
    "Feature Selection",
    "Model Training",
    "Model Evaluation",
    "Prediction",
    "Streamlit Deployment"
]

for step_number, step in enumerate(workflow, start=1):

    st.write(f"**Step {step_number}:** {step}")

st.divider()
# ==========================================================
# MODEL INFORMATION
# ==========================================================

st.header("🧠 Model Information")

col1, col2 = st.columns(2)

with col1:

    st.subheader("Classification Model")

    st.write("""
The Iris Flower Classification model is a supervised Machine
Learning classification model trained on the Iris dataset.

The model learns the relationship between flower measurements
and species labels, allowing it to predict the species of new
flowers with high accuracy.
""")

with col2:

    st.subheader("Prediction Process")

    st.write("""
1. User enters flower measurements.

2. Values are passed to the trained model.

3. The model predicts the flower species.

4. Prediction confidence is calculated.

5. Results are displayed with visualizations.
""")

st.divider()

# ==========================================================
# TECHNOLOGIES USED
# ==========================================================

st.header("🛠 Technologies Used")

tech_df = pd.DataFrame({

    "Technology":[
        "Python",
        "Streamlit",
        "Scikit-learn",
        "Pandas",
        "NumPy",
        "Matplotlib",
        "Pickle"
    ],

    "Purpose":[
        "Programming Language",
        "Interactive Dashboard",
        "Machine Learning",
        "Data Manipulation",
        "Numerical Computing",
        "Data Visualization",
        "Model Serialization"
    ]

})

st.dataframe(
    tech_df,
    use_container_width=True
)

st.divider()

# ==========================================================
# DASHBOARD FEATURES
# ==========================================================

st.header("✨ Dashboard Features")

feature_col1, feature_col2 = st.columns(2)

with feature_col1:

    st.success("""
### Core Features

✔ Analytics Dashboard

✔ Flower Prediction

✔ Model Comparison

✔ Prediction History

✔ Interactive Charts

✔ CSV Download
""")

with feature_col2:

    st.info("""
### User Experience

✔ Clean Interface

✔ Responsive Layout

✔ Fast Prediction

✔ Easy Navigation

✔ Professional Design

✔ Portfolio Ready
""")

st.divider()

# ==========================================================
# SKILLS DEMONSTRATED
# ==========================================================

st.header("💼 Skills Demonstrated")

skills = [
    "Python Programming",
    "Machine Learning",
    "Classification Algorithms",
    "Data Visualization",
    "Data Analysis",
    "Feature Engineering",
    "Model Deployment",
    "Streamlit Development",
    "Dashboard Design",
    "Problem Solving"
]

skill_cols = st.columns(2)

for i, skill in enumerate(skills):

    if i % 2 == 0:
        skill_cols[0].write(f"✅ {skill}")
    else:
        skill_cols[1].write(f"✅ {skill}")

st.divider()

# ==========================================================
# FUTURE IMPROVEMENTS
# ==========================================================

st.header("🚀 Future Improvements")

future_df = pd.DataFrame({

    "Future Feature":[
        "Deep Learning Model",
        "Cloud Deployment",
        "Multiple Dataset Support",
        "Real-Time Prediction API",
        "User Authentication",
        "Database Integration",
        "Advanced Visualizations",
        "Mobile Responsive UI"
    ]

})

st.dataframe(
    future_df,
    use_container_width=True
)

st.divider()

# ==========================================================
# PROJECT HIGHLIGHTS
# ==========================================================

st.header("🏆 Project Highlights")

metric1, metric2, metric3, metric4 = st.columns(4)

metric1.metric("Dataset", "150 Samples")
metric2.metric("Features", "4")
metric3.metric("Classes", "3")
metric4.metric("Dashboard Pages", "4")

st.divider()

# ==========================================================
# DEVELOPER INFORMATION
# ==========================================================

st.header("👩‍💻 Developer")

st.markdown("""
This dashboard was developed as a Data Science portfolio project
to demonstrate practical knowledge of:

- Machine Learning
- Data Analysis
- Interactive Dashboard Development
- Streamlit Framework
- Data Visualization
- Python Programming

The project is designed to provide a complete workflow from
data exploration to intelligent prediction using a trained
machine learning model.
""")

st.divider()

# ==========================================================
# THANK YOU MESSAGE
# ==========================================================

st.markdown(
    """
    <div style="
        background-color:#f8f9fa;
        padding:25px;
        border-radius:12px;
        border-left:6px solid #6C63FF;
        text-align:center;
    ">

    <h2>🌸 Thank You for Visiting</h2>

    <p style="font-size:16px;">
    Thank you for exploring the <b>Smart Iris Flower Classification Dashboard</b>.

    This project demonstrates how Machine Learning, Data Analysis,
    and Interactive Visualization can be combined into a professional
    web application using Python and Streamlit.
    </p>

    <p style="color:gray;">
    Keep Learning • Keep Building • Keep Growing 🚀
    </p>

    </div>
    """,
    unsafe_allow_html=True
)