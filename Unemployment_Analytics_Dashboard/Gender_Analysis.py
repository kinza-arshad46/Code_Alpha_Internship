# ==========================================================
# Gender Analysis Page
# ==========================================================

import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================================
# Page Config
# ==========================================================

st.set_page_config(
    page_title="Gender Analysis",
    page_icon="👥",
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
# Header
# ==========================================================

st.markdown("""
<div class="title">

👥 Gender Analysis

</div>
""", unsafe_allow_html=True)

st.write(
"""
Compare unemployment trends between males and females across different years and age categories.
"""
)

st.markdown("---")

# ==========================================================
# Sidebar Filters
# ==========================================================

st.sidebar.header("🎛 Filters")

country = st.sidebar.selectbox(
    "🌍 Country",
    ["All"] + sorted(df["country"].unique())
)

years = st.sidebar.multiselect(
    "📅 Select Years",
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

filtered_df = filtered_df[
    filtered_df["year"].isin(years)
]

# ==========================================================
# KPI Cards
# ==========================================================

male_avg = filtered_df[
    filtered_df["gender"] == "Male"
]["unemployment_rate"].mean()

female_avg = filtered_df[
    filtered_df["gender"] == "Female"
]["unemployment_rate"].mean()

difference = female_avg - male_avg

records = len(filtered_df)

c1, c2, c3, c4 = st.columns(4)

c1.metric("📄 Records", records)
c2.metric("👨 Male Avg", f"{male_avg:.2f}%")
c3.metric("👩 Female Avg", f"{female_avg:.2f}%")
c4.metric("📊 Difference", f"{difference:.2f}%")

st.markdown("---")

# ==========================================================
# Trend Analysis
# ==========================================================

st.subheader("📈 Gender-wise Trend")

trend = (
    filtered_df
    .groupby(["year", "gender"])["unemployment_rate"]
    .mean()
    .reset_index()
)

fig = px.line(
    trend,
    x="year",
    y="unemployment_rate",
    color="gender",
    markers=True,
    title="Male vs Female Unemployment Trend"
)

fig.update_layout(
    template="plotly_white",
    title_x=0.5,
    height=500
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ==========================================================
# Bar Chart
# ==========================================================

left, right = st.columns(2)

with left:

    gender_avg = (
        filtered_df
        .groupby("gender")["unemployment_rate"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        gender_avg,
        x="gender",
        y="unemployment_rate",
        color="gender",
        text_auto=".2f",
        title="Average Unemployment by Gender"
    )

    fig.update_layout(
        template="plotly_white",
        title_x=0.5
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

    fig = px.pie(
        gender_avg,
        names="gender",
        values="unemployment_rate",
        hole=0.5,
        title="Gender Distribution"
    )

    fig.update_layout(
        template="plotly_white",
        title_x=0.5
    )

    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ==========================================================
# Age Category Comparison
# ==========================================================

st.subheader("🧒 Gender by Age Category")

age_gender = (
    filtered_df
    .groupby(["age_category", "gender"])["unemployment_rate"]
    .mean()
    .reset_index()
)

fig = px.bar(
    age_gender,
    x="age_category",
    y="unemployment_rate",
    color="gender",
    barmode="group",
    text_auto=".2f",
    title="Gender Comparison Across Age Categories"
)

fig.update_layout(
    template="plotly_white",
    title_x=0.5,
    height=500
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ==========================================================
# Covid Impact
# ==========================================================

st.subheader("🦠 Covid-19 Gender Impact")

covid_df = filtered_df[
    filtered_df["year"] >= 2019
]

fig = px.line(
    covid_df,
    x="year",
    y="unemployment_rate",
    color="gender",
    markers=True,
    title="Gender-wise Covid Impact"
)

fig.update_layout(
    template="plotly_white",
    title_x=0.5,
    height=500
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ==========================================================
# Data Preview
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
    "📥 Download Filtered Data",
    data=csv,
    file_name="gender_analysis.csv",
    mime="text/csv"
)

st.markdown("---")

# ==========================================================
# Insights
# ==========================================================

higher_gender = "Female" if female_avg > male_avg else "Male"

st.info(
    f"""
### 📌 Key Insight

- **{higher_gender}** has the higher average unemployment rate in the selected data.
- Compare trends across years to observe how unemployment changed over time.
- The Covid-19 section highlights gender-specific changes after 2019.
"""
)

st.markdown("---")

# ==========================================================
# Footer
# ==========================================================

st.markdown(
"""
<div style="text-align:center;color:gray">

Gender Analysis • Streamlit Dashboard

</div>
""",
unsafe_allow_html=True
)