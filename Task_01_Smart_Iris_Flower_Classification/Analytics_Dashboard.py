
# Smart Iris Flower Classification & Analytics Dashboard
# Analytics Dashboard
# Import Libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# Load CSS
# -----------------------------
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -----------------------------
# Title
# -----------------------------
st.markdown("<h1 class='main-title'>📊 Analytics Dashboard</h1>", unsafe_allow_html=True)
st.markdown("Analyze your dataset with interactive statistics and visualizations.")

st.divider()

# -----------------------------
# Upload Dataset
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload CSV Dataset",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    # Save in session state
    st.session_state["df"] = df

    # -----------------------------
    # Basic Info
    # -----------------------------
    st.subheader("📁 Dataset Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric("Missing Values", int(df.isnull().sum().sum()))
    col4.metric("Duplicates", int(df.duplicated().sum()))

    st.divider()

    # -----------------------------
    # Dataset Preview
    # -----------------------------
    st.subheader("👀 Preview")

    st.dataframe(
        df.head(10),
        use_container_width=True
    )

    st.divider()

    # -----------------------------
    # Data Types
    # -----------------------------
    st.subheader("📌 Data Types")

    dtype_df = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str)
    })

    st.dataframe(dtype_df, use_container_width=True)

    st.divider()

    # -----------------------------
    # Summary Statistics
    # -----------------------------
    st.subheader("📈 Summary Statistics")

    st.dataframe(
        df.describe(include="all").T,
        use_container_width=True
    )

    st.divider()

    # -----------------------------
    # Missing Values
    # -----------------------------
    st.subheader("❗ Missing Values")

    missing = df.isnull().sum()

    missing_df = pd.DataFrame({
        "Column": missing.index,
        "Missing": missing.values
    })

    st.dataframe(
        missing_df,
        use_container_width=True
    )

    # Bar Chart

    fig, ax = plt.subplots(figsize=(10,4))

    sns.barplot(
        data=missing_df,
        x="Column",
        y="Missing",
        ax=ax
    )

    plt.xticks(rotation=45)

    st.pyplot(fig)

    st.divider()

    # -----------------------------
    # Correlation Heatmap
    # -----------------------------
    numeric_df = df.select_dtypes(include=np.number)

    if len(numeric_df.columns) >= 2:

        st.subheader("🔥 Correlation Heatmap")

        corr = numeric_df.corr()

        fig, ax = plt.subplots(figsize=(10,6))

        sns.heatmap(
            corr,
            annot=True,
            cmap="coolwarm",
            linewidths=.5,
            ax=ax
        )

        st.pyplot(fig)

    st.divider()

    # -----------------------------
    # Feature Distribution
    # -----------------------------
    st.subheader("📊 Feature Distribution")

    numeric_cols = numeric_df.columns.tolist()

    if len(numeric_cols):

        feature = st.selectbox(
            "Select Numeric Feature",
            numeric_cols
        )

        fig, ax = plt.subplots(figsize=(8,4))

        sns.histplot(
            df[feature],
            kde=True,
            bins=25,
            ax=ax
        )

        st.pyplot(fig)

    st.divider()

    # -----------------------------
    # Box Plot
    # -----------------------------
    st.subheader("📦 Box Plot")

    if len(numeric_cols):

        feature = st.selectbox(
            "Choose Feature",
            numeric_cols,
            key="box"
        )

        fig, ax = plt.subplots(figsize=(8,4))

        sns.boxplot(
            x=df[feature],
            ax=ax
        )

        st.pyplot(fig)

    st.divider()

    # -----------------------------
    # Value Counts
    # -----------------------------
    st.subheader("📋 Categorical Analysis")

    categorical = df.select_dtypes(include="object").columns.tolist()

    if len(categorical):

        column = st.selectbox(
            "Choose Column",
            categorical
        )

        vc = df[column].value_counts()

        st.dataframe(vc)

        fig, ax = plt.subplots(figsize=(8,4))

        sns.countplot(
            data=df,
            x=column,
            ax=ax
        )

        plt.xticks(rotation=45)

        st.pyplot(fig)

    st.divider()

    # -----------------------------
    # Download Report
    # -----------------------------
    st.subheader("📄 Download Summary")

    report = df.describe(include="all").T

    csv = report.to_csv().encode("utf-8")

    st.download_button(
        label="⬇ Download Summary Report",
        data=csv,
        file_name="summary_report.csv",
        mime="text/csv"
    )

else:

    st.info("Upload a CSV file to begin analysis.")