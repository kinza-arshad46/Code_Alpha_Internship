# ==========================================================
# Covid-19 Impact Analysis
# ==========================================================

import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================================
# Page Config
# ==========================================================

st.set_page_config(
    page_title="Covid-19 Impact",
    page_icon="🦠",
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

🦠 Covid-19 Impact Analysis

</div>
""", unsafe_allow_html=True)

st.write(
"""
Analyze unemployment before, during, and after the Covid-19 pandemic.
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

gender = st.sidebar.selectbox(
    "👥 Gender",
    ["All"] + sorted(df["gender"].unique())
)

if country != "All":
    df = df[df["country"] == country]

if gender != "All":
    df = df[df["gender"] == gender]

# ==========================================================
# Covid Period Labels
# ==========================================================

df["period"] = "After Covid"

df.loc[df["year"] <= 2019, "period"] = "Before Covid"
df.loc[df["year"].isin([2020, 2021]), "period"] = "During Covid"

# ==========================================================
# KPI Cards
# ==========================================================

before = df[df["period"] == "Before Covid"]["unemployment_rate"].mean()
during = df[df["period"] == "During Covid"]["unemployment_rate"].mean()
after = df[df["period"] == "After Covid"]["unemployment_rate"].mean()

change = ((during - before) / before) * 100

c1, c2, c3, c4 = st.columns(4)

c1.metric("📉 Before Covid", f"{before:.2f}%")
c2.metric("🦠 During Covid", f"{during:.2f}%")
c3.metric("📈 After Covid", f"{after:.2f}%")
c4.metric("📊 Increase", f"{change:.1f}%")

st.markdown("---")

# ==========================================================
# Before vs During vs After
# ==========================================================

period_df = (
    df.groupby("period")["unemployment_rate"]
      .mean()
      .reset_index()
)

fig = px.bar(
    period_df,
    x="period",
    y="unemployment_rate",
    color="period",
    text_auto=".2f",
    title="Average Unemployment by Covid Period"
)

fig.update_layout(
    template="plotly_white",
    title_x=.5,
    showlegend=False,
    height=500
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ==========================================================
# Trend
# ==========================================================

trend = (
    df.groupby("year")["unemployment_rate"]
      .mean()
      .reset_index()
)

fig = px.line(
    trend,
    x="year",
    y="unemployment_rate",
    markers=True,
    title="Yearly Unemployment Trend"
)

fig.add_vrect(
    x0=2019.5,
    x1=2021.5,
    fillcolor="red",
    opacity=0.15,
    line_width=0,
    annotation_text="Covid Period"
)

fig.update_layout(
    template="plotly_white",
    title_x=.5,
    height=500
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ==========================================================
# Gender Impact
# ==========================================================

gender_period = (
    df.groupby(["period", "gender"])["unemployment_rate"]
      .mean()
      .reset_index()
)

fig = px.bar(
    gender_period,
    x="period",
    y="unemployment_rate",
    color="gender",
    barmode="group",
    text_auto=".2f",
    title="Covid Impact by Gender"
)

fig.update_layout(
    template="plotly_white",
    title_x=.5,
    height=500
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ==========================================================
# Age Group Impact
# ==========================================================

age_period = (
    df.groupby(["period", "age_category"])["unemployment_rate"]
      .mean()
      .reset_index()
)

fig = px.bar(
    age_period,
    x="period",
    y="unemployment_rate",
    color="age_category",
    barmode="group",
    text_auto=".2f",
    title="Covid Impact by Age Group"
)

fig.update_layout(
    template="plotly_white",
    title_x=.5,
    height=500
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ==========================================================
# Top 10 Affected Countries
# ==========================================================

country_df = (
    df[df["period"] == "During Covid"]
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
    title="Top 10 Countries During Covid"
)

fig.update_layout(
    template="plotly_white",
    title_x=.5,
    coloraxis_showscale=False,
    height=550
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ==========================================================
# Data Preview
# ==========================================================

st.subheader("📄 Filtered Dataset")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

# ==========================================================
# Download
# ==========================================================

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Download Covid Analysis",
    csv,
    "covid_analysis.csv",
    "text/csv"
)

st.markdown("---")

# ==========================================================
# Key Insights
# ==========================================================

st.info(f"""
### 📌 Key Insights

- Average unemployment before Covid: **{before:.2f}%**
- Average unemployment during Covid: **{during:.2f}%**
- Average unemployment after Covid: **{after:.2f}%**
- Covid caused an average increase of **{change:.1f}%** in unemployment.
- Compare charts to identify the most affected countries, genders, and age groups.
""")

st.markdown("---")

# ==========================================================
# Footer
# ==========================================================

st.markdown("""
<div style="text-align:center;color:gray">

Covid-19 Impact Analysis • Streamlit Dashboard

</div>
""", unsafe_allow_html=True)