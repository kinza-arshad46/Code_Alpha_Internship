# ==========================================================
# Age Group Analysis Page
# ==========================================================

import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================================
# Page Config
# ==========================================================

st.set_page_config(
    page_title="Age Group Analysis",
    page_icon="🧒",
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

🧒 Age Group Analysis

</div>
""", unsafe_allow_html=True)

st.write(
"""
Explore unemployment trends across Children, Youth, and Adults.
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

if gender != "All":
    filtered_df = filtered_df[
        filtered_df["gender"] == gender
    ]

filtered_df = filtered_df[
    filtered_df["year"].isin(years)
]

# ==========================================================
# KPI Cards
# ==========================================================

avg_rate = filtered_df["unemployment_rate"].mean()
highest = filtered_df["unemployment_rate"].max()
lowest = filtered_df["unemployment_rate"].min()
groups = filtered_df["age_category"].nunique()

c1, c2, c3, c4 = st.columns(4)

c1.metric("🧒 Age Groups", groups)
c2.metric("📈 Average", f"{avg_rate:.2f}%")
c3.metric("🔺 Highest", f"{highest:.2f}%")
c4.metric("🔻 Lowest", f"{lowest:.2f}%")

st.markdown("---")

# ==========================================================
# Trend by Age Group
# ==========================================================

st.subheader("📈 Age Group Trend")

trend = (
    filtered_df
    .groupby(["year", "age_category"])["unemployment_rate"]
    .mean()
    .reset_index()
)

fig = px.line(
    trend,
    x="year",
    y="unemployment_rate",
    color="age_category",
    markers=True,
    title="Unemployment Trend by Age Group"
)

fig.update_layout(
    template="plotly_white",
    title_x=0.5,
    height=500
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ==========================================================
# Average by Age Group
# ==========================================================

left, right = st.columns(2)

with left:

    avg_df = (
        filtered_df
        .groupby("age_category")["unemployment_rate"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        avg_df,
        x="age_category",
        y="unemployment_rate",
        color="age_category",
        text_auto=".2f",
        title="Average Unemployment by Age Group"
    )

    fig.update_layout(
        template="plotly_white",
        title_x=0.5,
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

    fig = px.box(
        filtered_df,
        x="age_category",
        y="unemployment_rate",
        color="age_category",
        title="Distribution by Age Group"
    )

    fig.update_layout(
        template="plotly_white",
        title_x=0.5
    )

    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ==========================================================
# Gender vs Age Group
# ==========================================================

st.subheader("👥 Gender vs Age Group")

gender_age = (
    filtered_df
    .groupby(["age_category", "gender"])["unemployment_rate"]
    .mean()
    .reset_index()
)

fig = px.bar(
    gender_age,
    x="age_category",
    y="unemployment_rate",
    color="gender",
    barmode="group",
    text_auto=".2f",
    title="Gender Comparison Across Age Groups"
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

st.subheader("🦠 Covid-19 Impact by Age Group")

covid_df = filtered_df[
    filtered_df["year"] >= 2019
]

fig = px.line(
    covid_df,
    x="year",
    y="unemployment_rate",
    color="age_category",
    markers=True,
    title="Covid-19 Impact on Age Groups"
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

st.subheader("🔥 Heatmap")

heatmap = (
    filtered_df
    .pivot_table(
        index="age_category",
        columns="year",
        values="unemployment_rate",
        aggfunc="mean"
    )
)

fig = px.imshow(
    heatmap,
    text_auto=".1f",
    aspect="auto",
    title="Average Unemployment Heatmap"
)

fig.update_layout(
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
# Download
# ==========================================================

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Download Filtered Data",
    data=csv,
    file_name="age_group_analysis.csv",
    mime="text/csv"
)

st.markdown("---")

# ==========================================================
# Insight
# ==========================================================

highest_group = (
    avg_df.loc[
        avg_df["unemployment_rate"].idxmax(),
        "age_category"
    ]
)

st.info(
f"""
### 📌 Key Insight

- **{highest_group}** has the highest average unemployment in the selected data.
- Compare trends to understand which age groups were most affected during Covid-19.
- Use the heatmap to identify years with relatively higher unemployment.
"""
)

st.markdown("---")

# ==========================================================
# Footer
# ==========================================================

st.markdown(
"""
<div style="text-align:center;color:gray">

Age Group Analysis • Streamlit Dashboard

</div>
""",
unsafe_allow_html=True
)