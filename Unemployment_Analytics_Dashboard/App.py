# ==========================================
# Global Unemployment Analytics Dashboard
# ==========================================

import streamlit as st
import pandas as pd

# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Global Unemployment Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# Load Custom CSS
# ==========================================

def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# ==========================================
# Load Dataset
# ==========================================

@st.cache_data
def load_data():
    return pd.read_csv("Final_Unemployment_Analysis.csv")

df = load_data()

# ==========================================
# Sidebar
# ==========================================

st.sidebar.title("🌍 Navigation")

st.sidebar.markdown("---")

st.sidebar.success("Dataset Loaded Successfully")

st.sidebar.info(
"""
### Dashboard Sections

📊 Dashboard

🌍 Country Analysis

👥 Gender Analysis

🧒 Age Group Analysis

🦠 Covid Impact

📈 Trend Analysis

📑 Key Insights
"""
)

st.sidebar.markdown("---")

st.sidebar.write("### Dataset Summary")

st.sidebar.write(f"Countries : **{df['country'].nunique()}**")

st.sidebar.write(f"Records : **{len(df)}**")

st.sidebar.write(f"Years : **{df['year'].min()} - {df['year'].max()}**")

# ==========================================
# Header
# ==========================================

st.markdown("""
<div class="title">

🌍 Global Unemployment Analytics Dashboard

</div>
""", unsafe_allow_html=True)

st.markdown(
"""
### Analyze Global Unemployment Trends (2014–2024)

This dashboard provides an interactive analysis of global unemployment trends across different countries, genders, and age groups. It also highlights the impact of Covid-19 on employment using visual analytics.

"""
)

st.markdown("---")

# ==========================================
# KPI Calculations
# ==========================================

total_records = len(df)

total_countries = df["country"].nunique()

average_rate = df["unemployment_rate"].mean()

highest_rate = df["unemployment_rate"].max()

lowest_rate = df["unemployment_rate"].min()

latest_year = df["year"].max()

# ==========================================
# KPI Cards
# ==========================================

st.subheader("📊 Dashboard Summary")

col1, col2, col3 = st.columns(3)

col1.metric(
    "🌍 Countries",
    total_countries
)

col2.metric(
    "📄 Records",
    total_records
)

col3.metric(
    "📅 Latest Year",
    latest_year
)

col4, col5, col6 = st.columns(3)

col4.metric(
    "📈 Average Rate",
    f"{average_rate:.2f}%"
)

col5.metric(
    "🔺 Highest Rate",
    f"{highest_rate:.2f}%"
)

col6.metric(
    "🔻 Lowest Rate",
    f"{lowest_rate:.2f}%"
)

st.markdown("---")

# ==========================================
# Dataset Preview
# ==========================================

st.subheader("📄 Dataset Preview")

st.dataframe(
    df.head(10),
    use_container_width=True
)

st.markdown("---")

# ==========================================
# About Project
# ==========================================

st.subheader("📌 About This Project")

st.write(
"""
This project analyzes unemployment trends using Python, Pandas, Plotly, and Streamlit.

### Dashboard Features

- 🌍 Country-wise Analysis
- 👥 Gender-wise Analysis
- 🧒 Age Group Analysis
- 🦠 Covid-19 Impact
- 📈 Yearly Trend Analysis
- 📊 Interactive Charts
- 📑 Key Insights & Policy Recommendations

The dashboard is designed to help understand unemployment patterns and support data-driven economic and social policy decisions.
"""
)

st.markdown("---")

# ==========================================
# Footer
# ==========================================

st.markdown(
"""
<center>

Developed with ❤️ using Streamlit | Pandas | Plotly | Python

</center>
""",
unsafe_allow_html=True
)