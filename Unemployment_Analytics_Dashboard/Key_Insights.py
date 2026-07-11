# ==========================================================
# Key Insights & Policy Recommendations
# ==========================================================

import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================================
# Page Config
# ==========================================================

st.set_page_config(
    page_title="Key Insights",
    page_icon="📑",
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

📑 Key Insights & Recommendations

</div>
""", unsafe_allow_html=True)

st.write(
"""
This page summarizes the major findings from the unemployment analysis and presents recommendations that may support policy and decision-making.
"""
)

st.markdown("---")

# ==========================================================
# KPI Cards
# ==========================================================

countries = df["country"].nunique()
records = len(df)
avg_rate = df["unemployment_rate"].mean()
latest_year = df["year"].max()

c1, c2, c3, c4 = st.columns(4)

c1.metric("🌍 Countries", countries)
c2.metric("📄 Records", records)
c3.metric("📈 Average Rate", f"{avg_rate:.2f}%")
c4.metric("📅 Latest Year", latest_year)

st.markdown("---")

# ==========================================================
# Top 5 Highest Countries
# ==========================================================

left, right = st.columns(2)

with left:

    st.subheader("🔺 Top 5 Highest Average Unemployment")

    highest = (
        df.groupby("country")["unemployment_rate"]
        .mean()
        .sort_values(ascending=False)
        .head(5)
        .reset_index()
    )

    fig = px.bar(
        highest,
        x="country",
        y="unemployment_rate",
        color="unemployment_rate",
        text_auto=".2f"
    )

    fig.update_layout(
        template="plotly_white",
        title_x=0.5,
        showlegend=False
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    st.subheader("🔻 Top 5 Lowest Average Unemployment")

    lowest = (
        df.groupby("country")["unemployment_rate"]
        .mean()
        .sort_values()
        .head(5)
        .reset_index()
    )

    fig = px.bar(
        lowest,
        x="country",
        y="unemployment_rate",
        color="unemployment_rate",
        text_auto=".2f"
    )

    fig.update_layout(
        template="plotly_white",
        title_x=0.5,
        showlegend=False
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.markdown("---")

# ==========================================================
# Executive Summary
# ==========================================================

st.subheader("📌 Executive Summary")

st.success("""
✅ Global unemployment varies significantly across countries.

✅ Youth generally experience higher unemployment than adults.

✅ Female unemployment is higher than male unemployment in many countries.

✅ A noticeable rise in unemployment occurred during the Covid-19 period.

✅ Several countries showed gradual recovery after the pandemic, while others continued to face elevated unemployment levels.
""")

st.markdown("---")

# ==========================================================
# Policy Recommendations
# ==========================================================

st.subheader("💡 Policy Recommendations")

st.info("""
### Employment Policies

• Increase investment in youth employment programs.

• Strengthen vocational and technical training.

• Support women through gender-inclusive employment initiatives.

• Expand digital skills training to prepare workers for future jobs.

• Encourage entrepreneurship and support small businesses.

• Improve labor market monitoring using real-time unemployment indicators.

• Develop emergency employment support programs during future crises.
""")

st.markdown("---")

# ==========================================================
# Project Summary
# ==========================================================

st.subheader("📊 Project Summary")

summary = pd.DataFrame({

    "Analysis Completed":[
        "Data Cleaning",
        "Exploratory Data Analysis",
        "Country Analysis",
        "Gender Analysis",
        "Age Group Analysis",
        "Covid-19 Impact",
        "Trend Analysis",
        "Interactive Dashboard"
    ],

    "Status":[
        "✅",
        "✅",
        "✅",
        "✅",
        "✅",
        "✅",
        "✅",
        "✅"
    ]

})

st.dataframe(
    summary,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

# ==========================================================
# Download Summary
# ==========================================================

summary_csv = summary.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Download Project Summary",
    summary_csv,
    "project_summary.csv",
    "text/csv"
)

st.markdown("---")

# ==========================================================
# Final Conclusion
# ==========================================================

st.subheader("🎯 Conclusion")

st.success("""
This dashboard successfully analyzes global unemployment trends between 2014 and 2024.

Using interactive visualizations, it explores unemployment patterns across countries, genders, and age groups while highlighting the impact of the Covid-19 pandemic.

The findings provide valuable insights that can support policymakers, researchers, and decision-makers in understanding labor market challenges and designing effective employment strategies.
""")

st.markdown("---")

# ==========================================================
# Footer
# ==========================================================

st.markdown(
"""
<div style="text-align:center;color:gray">

Global Unemployment Analytics Dashboard

Built with ❤️ using Python • Pandas • Plotly • Streamlit

</div>
""",
unsafe_allow_html=True
)