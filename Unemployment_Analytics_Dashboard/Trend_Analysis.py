# ==========================================================
# Trend Analysis Page
# ==========================================================

import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================================
# Page Config
# ==========================================================

st.set_page_config(
    page_title="Trend Analysis",
    page_icon="📈",
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

📈 Trend Analysis

</div>
""", unsafe_allow_html=True)

st.write(
"""
Analyze long-term unemployment trends using moving averages, yearly changes, and growth analysis.
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
# Yearly Trend
# ==========================================================

trend = (
    df.groupby("year")["unemployment_rate"]
      .mean()
      .reset_index()
)

trend["Moving Average"] = (
    trend["unemployment_rate"]
    .rolling(3)
    .mean()
)

trend["Yearly Change"] = (
    trend["unemployment_rate"]
    .diff()
)

trend["Growth %"] = (
    trend["unemployment_rate"]
    .pct_change() * 100
)

# ==========================================================
# KPI Cards
# ==========================================================

avg = trend["unemployment_rate"].mean()
highest = trend["unemployment_rate"].max()
lowest = trend["unemployment_rate"].min()
growth = trend["Growth %"].mean()

c1, c2, c3, c4 = st.columns(4)

c1.metric("📈 Average", f"{avg:.2f}%")
c2.metric("🔺 Highest", f"{highest:.2f}%")
c3.metric("🔻 Lowest", f"{lowest:.2f}%")
c4.metric("📊 Avg Growth", f"{growth:.2f}%")

st.markdown("---")

# ==========================================================
# Actual vs Moving Average
# ==========================================================

fig = px.line(
    trend,
    x="year",
    y=["unemployment_rate", "Moving Average"],
    markers=True,
    title="Actual Trend vs Moving Average"
)

fig.update_layout(
    template="plotly_white",
    title_x=0.5,
    height=550
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ==========================================================
# Yearly Change
# ==========================================================

fig = px.bar(
    trend,
    x="year",
    y="Yearly Change",
    text_auto=".2f",
    color="Yearly Change",
    title="Year-over-Year Change"
)

fig.update_layout(
    template="plotly_white",
    title_x=0.5,
    coloraxis_showscale=False,
    height=500
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ==========================================================
# Growth Rate
# ==========================================================

fig = px.line(
    trend,
    x="year",
    y="Growth %",
    markers=True,
    title="Yearly Growth Rate (%)"
)

fig.update_layout(
    template="plotly_white",
    title_x=0.5,
    height=500
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ==========================================================
# Heatmap
# ==========================================================

pivot = (
    df.pivot_table(
        index="gender",
        columns="year",
        values="unemployment_rate",
        aggfunc="mean"
    )
)

fig = px.imshow(
    pivot,
    text_auto=".1f",
    aspect="auto",
    title="Gender-wise Heatmap"
)

fig.update_layout(
    title_x=0.5,
    height=450
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ==========================================================
# Trend Table
# ==========================================================

st.subheader("📄 Trend Statistics")

st.dataframe(
    trend,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

# ==========================================================
# Download
# ==========================================================

csv = trend.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Download Trend Analysis",
    csv,
    "trend_analysis.csv",
    "text/csv"
)

st.markdown("---")

# ==========================================================
# Key Insights
# ==========================================================

max_year = trend.loc[
    trend["unemployment_rate"].idxmax(),
    "year"
]

min_year = trend.loc[
    trend["unemployment_rate"].idxmin(),
    "year"
]

st.info(f"""
### 📌 Trend Insights

- Highest average unemployment occurred in **{max_year}**.
- Lowest average unemployment occurred in **{min_year}**.
- The moving average smooths yearly fluctuations and reveals the long-term trend.
- Year-over-year change highlights periods of rapid increases or decreases.
- Growth rate indicates the relative annual change in unemployment.
""")

st.markdown("---")

# ==========================================================
# Footer
# ==========================================================

st.markdown("""
<div style="text-align:center;color:gray">

Trend Analysis • Streamlit Dashboard

</div>
""", unsafe_allow_html=True)