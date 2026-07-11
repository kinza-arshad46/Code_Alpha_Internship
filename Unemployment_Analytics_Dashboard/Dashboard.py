# ==========================================================
# Dashboard Page
# Global Unemployment Analytics Dashboard
# ==========================================================

import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================================
# Page Config
# ==========================================================

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

# ==========================================================
# Load CSS
# ==========================================================

def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# ==========================================================
# Load Dataset
# ==========================================================

@st.cache_data
def load_data():
    return pd.read_csv("Final_Unemployment_Analysis.csv")

df = load_data()

# ==========================================================
# Sidebar
# ==========================================================

st.sidebar.header("🎛 Dashboard Filters")

country = st.sidebar.selectbox(
    "🌍 Country",
    ["All"] + sorted(df["country"].unique())
)

gender = st.sidebar.selectbox(
    "👥 Gender",
    ["All"] + sorted(df["gender"].unique())
)

age = st.sidebar.selectbox(
    "🧒 Age Category",
    ["All"] + sorted(df["age_category"].unique())
)

year = st.sidebar.multiselect(
    "📅 Select Year",
    sorted(df["year"].unique()),
    default=sorted(df["year"].unique())
)

# ==========================================================
# Apply Filters
# ==========================================================

filtered_df = df.copy()

if country != "All":
    filtered_df = filtered_df[
        filtered_df["country"] == country
    ]

if gender != "All":
    filtered_df = filtered_df[
        filtered_df["gender"] == gender
    ]

if age != "All":
    filtered_df = filtered_df[
        filtered_df["age_category"] == age
    ]

filtered_df = filtered_df[
    filtered_df["year"].isin(year)
]

# ==========================================================
# Header
# ==========================================================

st.markdown(
"""
<div class="title">

📊 Dashboard Overview

</div>
""",
unsafe_allow_html=True
)

st.write(
"""
Analyze unemployment trends using interactive filters.
"""
)

st.markdown("---")

# ==========================================================
# KPI Calculations
# ==========================================================

total_records = len(filtered_df)

countries = filtered_df["country"].nunique()

avg_rate = filtered_df["unemployment_rate"].mean()

highest_rate = filtered_df["unemployment_rate"].max()

lowest_rate = filtered_df["unemployment_rate"].min()

latest_year = filtered_df["year"].max()

covid_avg = filtered_df[
    filtered_df["year"] == 2020
]["unemployment_rate"].mean()

# ==========================================================
# KPI Cards
# ==========================================================

st.subheader("📈 Dashboard Summary")

row1 = st.columns(4)

row1[0].metric(
    "📄 Records",
    f"{total_records:,}"
)

row1[1].metric(
    "🌍 Countries",
    countries
)

row1[2].metric(
    "📅 Latest Year",
    latest_year
)

row1[3].metric(
    "📈 Avg Rate",
    f"{avg_rate:.2f}%"
)

row2 = st.columns(3)

row2[0].metric(
    "🔺 Highest Rate",
    f"{highest_rate:.2f}%"
)

row2[1].metric(
    "🔻 Lowest Rate",
    f"{lowest_rate:.2f}%"
)

row2[2].metric(
    "🦠 Covid Avg (2020)",
    f"{covid_avg:.2f}%"
)

st.markdown("---")

# ==========================================================
# Yearly Trend
# ==========================================================

st.subheader("📈 Global Unemployment Trend")

trend = (
    filtered_df
    .groupby("year")["unemployment_rate"]
    .mean()
    .reset_index()
)

fig = px.line(
    trend,
    x="year",
    y="unemployment_rate",
    markers=True,
    title="Average Unemployment Rate by Year"
)

fig.update_layout(
    template="plotly_white",
    height=500,
    title_x=0.5
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

# ==========================================================
# Two Charts
# ==========================================================

left, right = st.columns(2)

# ----------------------------------------------------------
# Histogram
# ----------------------------------------------------------

with left:

    st.subheader("📊 Distribution")

    fig = px.histogram(
        filtered_df,
        x="unemployment_rate",
        nbins=30,
        title="Distribution of Unemployment Rate"
    )

    fig.update_layout(
        template="plotly_white",
        height=420,
        title_x=.5
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ----------------------------------------------------------
# Boxplot
# ----------------------------------------------------------

with right:

    st.subheader("📦 Outlier Detection")

    fig = px.box(
        filtered_df,
        y="unemployment_rate",
        color="gender",
        title="Unemployment Rate Boxplot"
    )

    fig.update_layout(
        template="plotly_white",
        height=420,
        title_x=.5
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.markdown("---")

# ==========================================================
# Gender Analysis
# ==========================================================

st.subheader("👥 Gender Distribution")

gender_df = (
    filtered_df
    .groupby("gender")["unemployment_rate"]
    .mean()
    .reset_index()
)

fig = px.pie(
    gender_df,
    names="gender",
    values="unemployment_rate",
    hole=.45,
    title="Average Unemployment Rate by Gender"
)

fig.update_layout(
    template="plotly_white",
    height=500,
    title_x=.5
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")
# ==========================================================
# Year-wise Average Unemployment
# ==========================================================

st.subheader("📅 Year-wise Average Unemployment Rate")

yearly_df = (
    filtered_df
    .groupby("year")["unemployment_rate"]
    .mean()
    .reset_index()
)

fig = px.bar(
    yearly_df,
    x="year",
    y="unemployment_rate",
    text_auto=".2f",
    color="unemployment_rate",
    title="Average Unemployment Rate by Year"
)

fig.update_layout(
    template="plotly_white",
    height=500,
    title_x=0.5,
    coloraxis_showscale=False
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

# ==========================================================
# Top 10 Countries
# ==========================================================

st.subheader("🌍 Top 10 Countries with Highest Average Unemployment")

country_df = (
    filtered_df
    .groupby("country")["unemployment_rate"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig = px.bar(
    country_df,
    x="country",
    y="unemployment_rate",
    color="unemployment_rate",
    text_auto=".2f",
    title="Top 10 Countries"
)

fig.update_layout(
    template="plotly_white",
    height=550,
    title_x=0.5,
    xaxis_title="Country",
    yaxis_title="Average Unemployment Rate (%)",
    coloraxis_showscale=False
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

# ==========================================================
# Age Category Analysis
# ==========================================================

st.subheader("🧒 Age Category Analysis")

age_df = (
    filtered_df
    .groupby("age_category")["unemployment_rate"]
    .mean()
    .reset_index()
)

fig = px.bar(
    age_df,
    x="age_category",
    y="unemployment_rate",
    color="age_category",
    text_auto=".2f",
    title="Average Unemployment Rate by Age Category"
)

fig.update_layout(
    template="plotly_white",
    height=500,
    title_x=0.5,
    showlegend=False
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

# ==========================================================
# Dataset Preview
# ==========================================================

st.subheader("📄 Filtered Dataset")

st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

# ==========================================================
# Download Button
# ==========================================================

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Filtered Dataset",
    data=csv,
    file_name="filtered_unemployment_data.csv",
    mime="text/csv"
)

st.markdown("---")

# ==========================================================
# Quick Dashboard Insights
# ==========================================================

st.subheader("📌 Dashboard Insights")

highest_country = (
    filtered_df
    .groupby("country")["unemployment_rate"]
    .mean()
    .idxmax()
)

highest_value = (
    filtered_df
    .groupby("country")["unemployment_rate"]
    .mean()
    .max()
)

lowest_country = (
    filtered_df
    .groupby("country")["unemployment_rate"]
    .mean()
    .idxmin()
)

lowest_value = (
    filtered_df
    .groupby("country")["unemployment_rate"]
    .mean()
    .min()
)

col1, col2 = st.columns(2)

with col1:
    st.info(
        f"""
### 📈 Highest Average Unemployment

**Country:** {highest_country}

**Average Rate:** {highest_value:.2f}%
"""
    )

with col2:
    st.success(
        f"""
### 📉 Lowest Average Unemployment

**Country:** {lowest_country}

**Average Rate:** {lowest_value:.2f}%
"""
    )

st.markdown("---")

# ==========================================================
# Project Information
# ==========================================================

with st.expander("ℹ️ About this Dashboard"):

    st.write(
        """
This dashboard provides an interactive analysis of global unemployment
data from **2014 to 2024**.

### Features

- 📊 Interactive Dashboard
- 🌍 Country Analysis
- 👥 Gender Analysis
- 🧒 Age Category Analysis
- 🦠 Covid-19 Impact Analysis
- 📈 Trend Analysis
- 📥 CSV Download

The dashboard is built using:

- Python
- Streamlit
- Pandas
- Plotly
"""
    )

st.markdown("---")

# ==========================================================
# Footer
# ==========================================================

st.markdown(
"""
<div style="text-align:center; padding:15px; color:gray;">

Developed with ❤️ using <b>Python</b> • <b>Streamlit</b> • <b>Pandas</b> • <b>Plotly</b>

</div>
""",
unsafe_allow_html=True
)