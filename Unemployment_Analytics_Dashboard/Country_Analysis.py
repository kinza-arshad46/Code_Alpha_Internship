# ==========================================================
# Country Analysis Page
# ==========================================================

import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================================
# Page Config
# ==========================================================

st.set_page_config(
    page_title="Country Analysis",
    page_icon="🌍",
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

🌍 Country Analysis

</div>
""", unsafe_allow_html=True)

st.write(
"Analyze unemployment trends for an individual country."
)

st.markdown("---")

# ==========================================================
# Country Selection
# ==========================================================

country = st.selectbox(
    "🌍 Select Country",
    sorted(df["country"].unique())
)

country_df = df[
    df["country"] == country
]

# ==========================================================
# KPI Cards
# ==========================================================

avg_rate = country_df["unemployment_rate"].mean()

highest_rate = country_df["unemployment_rate"].max()

lowest_rate = country_df["unemployment_rate"].min()

latest_year = country_df["year"].max()

records = len(country_df)

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric("📄 Records", records)
c2.metric("📈 Average", f"{avg_rate:.2f}%")
c3.metric("🔺 Highest", f"{highest_rate:.2f}%")
c4.metric("🔻 Lowest", f"{lowest_rate:.2f}%")
c5.metric("📅 Latest Year", latest_year)

st.markdown("---")

# ==========================================================
# Yearly Trend
# ==========================================================

st.subheader("📈 Unemployment Trend")

trend = (
    country_df
    .groupby("year")["unemployment_rate"]
    .mean()
    .reset_index()
)

fig = px.line(
    trend,
    x="year",
    y="unemployment_rate",
    markers=True,
    title=f"{country} Unemployment Trend"
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
# Gender Analysis
# ==========================================================

left,right = st.columns(2)

with left:

    gender_df = (
        country_df
        .groupby("gender")["unemployment_rate"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        gender_df,
        x="gender",
        y="unemployment_rate",
        color="gender",
        text_auto=".2f",
        title="Gender Comparison"
    )

    fig.update_layout(
        template="plotly_white",
        title_x=.5
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    age_df = (
        country_df
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
        title="Age Category Comparison"
    )

    fig.update_layout(
        template="plotly_white",
        title_x=.5,
        showlegend=False
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.markdown("---")

# ==========================================================
# Covid Trend
# ==========================================================

st.subheader("🦠 Covid-19 Impact")

covid = country_df[
    country_df["year"] >= 2019
]

fig = px.line(
    covid,
    x="year",
    y="unemployment_rate",
    color="gender",
    markers=True,
    title="Covid Impact Analysis"
)

fig.update_layout(
    template="plotly_white",
    title_x=.5,
    height=500
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

# ==========================================================
# Dataset
# ==========================================================

st.subheader("📄 Country Dataset")

st.dataframe(
    country_df,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

# ==========================================================
# Download
# ==========================================================

csv = country_df.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Download Country Data",
    csv,
    f"{country}.csv",
    "text/csv"
)

st.markdown("---")

# ==========================================================
# Quick Insights
# ==========================================================

highest_year = trend.loc[
    trend["unemployment_rate"].idxmax(),
    "year"
]

st.info(
f"""
### 📌 Quick Insight

• Country Selected: **{country}**

• Highest unemployment was recorded in **{highest_year}**

• Average unemployment rate is **{avg_rate:.2f}%**

• The trend chart helps identify changes before and after Covid-19.
"""
)

st.markdown("---")

st.markdown(
"""
<div style="text-align:center;color:gray">

Country Analysis • Streamlit Dashboard

</div>
""",
unsafe_allow_html=True
)