import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os
from datetime import datetime
import matplotlib.pyplot as plt
import joblib

# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(
    page_title="Flower Predictor",
    page_icon="🌸",
    layout="wide"
)

# ======================================================
# LOAD CSS
# ======================================================

css_path = "style.css"

if os.path.exists(css_path):
    with open(css_path) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# ======================================================
# PAGE HEADER
# ======================================================

st.markdown(
    """
    <h1 style='text-align:center;color:#6C63FF;'>
    🌸 Iris Flower Predictor
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
"""
Predict Iris flower species using a trained Machine Learning model.
Enter flower measurements below and click **Predict**.
"""
)

st.divider()

# ======================================================
# LOAD MODEL
# ======================================================

@st.cache_resource
def load_model():
    model = joblib.load("iris_model.pkl")
    return model

model = load_model()

# ======================================================
# SIDEBAR
# ======================================================

st.sidebar.header("Prediction Guide")

st.sidebar.info(
"""
### Measurement Range

Sepal Length : 4.0 - 8.0 cm

Sepal Width : 2.0 - 4.5 cm

Petal Length : 1.0 - 7.0 cm

Petal Width : 0.1 - 2.5 cm
"""
)

st.sidebar.success(
"""
Tips

✔ Enter realistic values

✔ Adjust sliders

✔ Click Predict

✔ View confidence score
"""
)

# ======================================================
# INPUT SECTION
# ======================================================

st.subheader("Flower Measurements")

col1, col2 = st.columns(2)

with col1:

    sepal_length = st.slider(
        "Sepal Length (cm)",
        4.0,
        8.0,
        5.4,
        0.1
    )

    sepal_width = st.slider(
        "Sepal Width (cm)",
        2.0,
        4.5,
        3.4,
        0.1
    )

with col2:

    petal_length = st.slider(
        "Petal Length (cm)",
        1.0,
        7.0,
        1.5,
        0.1
    )

    petal_width = st.slider(
        "Petal Width (cm)",
        0.1,
        2.5,
        0.2,
        0.1
    )

st.divider()

# ======================================================
# CREATE INPUT ARRAY
# ======================================================

input_data = np.array([
    [
        sepal_length,
        sepal_width,
        petal_length,
        petal_width
    ]
])

# ======================================================
# PREDICT BUTTON
# ======================================================

predict = st.button(
    "🌸 Predict Flower",
    use_container_width=True
)

# ======================================================
# LABELS
# ======================================================

flower_names = {
    0: "Setosa",
    1: "Versicolor",
    2: "Virginica"
}

flower_description = {

    "Setosa":
    """
    ✔ Small flower

    ✔ Short petals

    ✔ Very easy to classify

    ✔ Usually found in colder regions.
    """,

    "Versicolor":
    """
    ✔ Medium-sized flower

    ✔ Moderate petal length

    ✔ Balanced characteristics

    ✔ Intermediate species.
    """,

    "Virginica":
    """
    ✔ Largest Iris species

    ✔ Long petals

    ✔ High petal width

    ✔ Most mature Iris flower.
    """
}

# ======================================================
# PREDICTION
# ======================================================

if predict:

    prediction = model.predict(input_data)[0]

    probabilities = model.predict_proba(input_data)[0]

    species = flower_names[prediction]

    confidence = np.max(probabilities) * 100

    st.success(
        f"Predicted Flower : {species}"
    )

    st.info(
        f"Confidence : {confidence:.2f}%"
    )

    st.divider()

        # ======================================================
    # FLOWER INFORMATION
    # ======================================================

    st.subheader("🌼 Prediction Details")

    col1, col2 = st.columns([1, 2])

    with col1:

        st.metric(
            label="Predicted Species",
            value=species
        )

        st.metric(
            label="Confidence",
            value=f"{confidence:.2f}%"
        )

    with col2:

        st.markdown("### Description")

        st.write(flower_description[species])

    st.divider()

    # ======================================================
    # PROBABILITY CHART
    # ======================================================

    st.subheader("📊 Prediction Probability")

    fig, ax = plt.subplots(figsize=(7,4))

    colors = ["#4CAF50", "#FFC107", "#F44336"]

    ax.bar(
        flower_names.values(),
        probabilities * 100,
        color=colors
    )

    ax.set_ylabel("Probability (%)")
    ax.set_ylim(0,100)

    for i, value in enumerate(probabilities):

        ax.text(
            i,
            value * 100 + 2,
            f"{value*100:.1f}%",
            ha="center",
            fontsize=10
        )

    st.pyplot(fig)

    st.divider()

    # ======================================================
    # INPUT SUMMARY
    # ======================================================

    st.subheader("📋 Input Measurements")

    summary = pd.DataFrame({

        "Feature":[
            "Sepal Length",
            "Sepal Width",
            "Petal Length",
            "Petal Width"
        ],

        "Value":[
            sepal_length,
            sepal_width,
            petal_length,
            petal_width
        ]

    })

    st.dataframe(
        summary,
        use_container_width=True
    )

    st.divider()

    # ======================================================
    # SAVE HISTORY
    # ======================================================

    history = pd.DataFrame({

        "Date":[datetime.now().strftime("%Y-%m-%d")],

        "Time":[datetime.now().strftime("%H:%M:%S")],

        "Sepal Length":[sepal_length],

        "Sepal Width":[sepal_width],

        "Petal Length":[petal_length],

        "Petal Width":[petal_width],

        "Prediction":[species],

        "Confidence":[round(confidence,2)]

    })

    history_file = "prediction_history.csv"

    if os.path.exists(history_file):

        old = pd.read_csv(history_file)

        history = pd.concat(
            [old, history],
            ignore_index=True
        )

    history.to_csv(
        history_file,
        index=False
    )

    # ======================================================
    # HISTORY TABLE
    # ======================================================

    st.subheader("🕒 Recent Predictions")

    history_df = pd.read_csv(history_file)

    st.dataframe(

        history_df.tail(10),

        use_container_width=True

    )

    st.divider()

    # ======================================================
    # DOWNLOAD BUTTON
    # ======================================================

    csv = history_df.to_csv(index=False).encode("utf-8")

    st.download_button(

        "⬇ Download Prediction History",

        csv,

        "prediction_history.csv",

        "text/csv",

        use_container_width=True

    )

    st.divider()

    # ======================================================
    # FOOTER
    # ======================================================

    st.markdown(
        """
        <div style="text-align:center;
                    padding:20px;
                    border-radius:10px;
                    background:#f5f5f5;">

        <h4>🎯 Machine Learning Prediction Completed</h4>

        <p>
        This prediction is generated using the trained
        Iris Flower Classification Machine Learning model.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )