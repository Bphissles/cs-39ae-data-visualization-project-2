import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
import utils

COLOR_THEMES = {
    "Ocean Blue": {
        "primary": "#1f77b4",
        "secondary": "#ff7f0e",
        "heatmap": "Blues",
    },
    "Sunset Warm": {
        "primary": "#e74c3c",
        "secondary": "#f39c12",
        "heatmap": "YlOrRd",
    },
    "Forest Green": {
        "primary": "#27ae60",
        "secondary": "#16a085",
        "heatmap": "Greens",
    },
    "Purple Haze": {
        "primary": "#9b59b6",
        "secondary": "#8e44ad",
        "heatmap": "Purples",
    },
    "Teal Mint": {
        "primary": "#16a085",
        "secondary": "#1abc9c",
        "heatmap": "YlGnBu",
    },
}

st.set_page_config(
    page_title="EDA Gallery - Developer Salaries | Professional Portfolio",
    page_icon="💎",
    layout="wide",
)

st.title("EDA Gallery – Developer Salaries")
st.caption(
    "Exploratory visualizations built from the 2024 developer salary dataset "
    "to answer key questions from the 5E Data Questioning Cycle."
)

data_path = Path(__file__).parent.parent / "data" / "developer-salary.csv"

try:
    df = pd.read_csv(data_path)
except Exception as e:
    st.error(f"Could not load data: {e}")
    st.info(f"Looking for CSV at: {data_path}")
    st.stop()

# Sidebar controls
with st.sidebar:
    st.header("🎨 Visualization Settings")
    color_theme = st.selectbox(
        "Color theme",
        options=list(COLOR_THEMES.keys()),
        index=0,
    )
    theme = COLOR_THEMES[color_theme]

    st.divider()
    st.header("📊 Data filters")

    exp_options = sorted(df["experience_level"].unique())
    selected_experience = st.multiselect(
        "Experience level",
        options=exp_options,
        default=[],
        help="Filter by experience level codes (EN, MI, SE, EX)",
    )

    year_options = sorted(df["work_year"].unique())
    selected_years = st.multiselect(
        "Work year",
        options=year_options,
        default=[],
    )

    remote_options = sorted(df["remote_ratio"].unique())
    remote_display = ["All"] + [str(r) for r in remote_options]
    selected_remote = st.selectbox(
        "Remote ratio",
        options=remote_display,
        index=0,
        help="Filter by remote ratio (0 = on-site, 50 = hybrid, 100 = fully remote)",
    )

df_filtered = df.copy()
if selected_experience:
    df_filtered = df_filtered[df_filtered["experience_level"].isin(selected_experience)]
if selected_years:
    df_filtered = df_filtered[df_filtered["work_year"].isin(selected_years)]
if selected_remote != "All":
    df_filtered = df_filtered[df_filtered["remote_ratio"] == int(selected_remote)]

st.markdown("---")

row1_col1, row1_col2 = st.columns(2)

with row1_col1:
    st.subheader("1. Salary by experience level")
    
    fig = px.box(
        df_filtered,
        x="experience_level",
        y="salary_in_usd",
        points=False,
        title="Salary by experience level",
        labels={
            "experience_level": "Level of professional experience (e.g., junior, mid, senior)",
            "salary_in_usd": "Salary (USD)",
        },
        color_discrete_sequence=[theme["primary"]],
    )
    fig.update_layout(
        showlegend=False,
        yaxis_tickformat="$,.0f",
        hovermode="closest",
    )
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown(
        """
        **Insight:** Median salaries rise consistently from entry-level to executive roles. However, senior positions exhibit significantly wider salary ranges and more extreme outliers compared to the tighter clustering seen in entry-level roles.
        """
    )

with row1_col2:
    st.subheader("2. Distribution of salaries")
    
    fig = px.histogram(
        df_filtered,
        x="salary_in_usd",
        nbins=40,
        title="Distribution of salaries",
        labels={"salary_in_usd": "Salary (USD)"},
        color_discrete_sequence=[theme["primary"]],
    )

    median_salary = df_filtered["salary_in_usd"].median()
    fig.add_vline(
        x=median_salary,
        line_dash="dash",
        line_color="orange",
        annotation_text="Median",
        annotation_position="top",
    )

    fig.update_layout(
        yaxis_title="Count",
        xaxis_tickformat="$,.0f",
        hovermode="x unified",
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown(
        """
        **Insight:** The salary distribution is right-skewed, indicating that while most roles cluster around the median, there is a long tail of high-earning outliers that extend significantly beyond the typical range.
        """
    )

row2_col1, row2_col2 = st.columns(2)

with row2_col1:
    st.subheader("3. Salary over time")
    
    medians = (
        df_filtered
        .groupby("work_year")["salary_in_usd"]
        .median()
        .sort_index()
        .reset_index()
    )

    fig = px.line(
        medians,
        x="work_year",
        y="salary_in_usd",
        markers=True,
        title="Salary over time (median salary by year)",
        labels={"work_year": "Work year", "salary_in_usd": "Median salary (USD)"},
        color_discrete_sequence=[theme["secondary"]],
    )

    fig.update_traces(name="Median salary", hovertemplate="Year=%{x}<br>Median=%{y:$,.0f}")
    fig.update_layout(
        hovermode="x unified",
        yaxis_tickformat="$,.0f",
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown(
        """
        **Insight:** Median salaries have shown a steady upward trend over the years, reflecting overall market growth, though the rate of increase appears to be stabilizing in the most recent data points.
        """
    )

with row2_col2:
    st.subheader("4. Remote vs on-site roles in 2024")
    
    df_2024 = df_filtered[df_filtered["work_year"] == 2024]
    df_remote = df_2024[df_2024["remote_ratio"].isin([0, 100])].copy()
    counts = (
        df_remote
        .groupby("remote_ratio")
        .size()
        .reset_index(name="count")
        .sort_values("remote_ratio")
    )

    fig = px.bar(
        counts,
        x="remote_ratio",
        y="count",
        title="Remote vs on-site roles in 2024",
        labels={"remote_ratio": "Remote ratio", "count": "Number of roles"},
        color_discrete_sequence=[theme["primary"]],
    )

    fig.update_traces(
        hovertemplate="Remote ratio=%{x}<br>Count=%{y}",
    )
    fig.update_layout(hovermode="x unified")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown(
        """
        **Insight:** In 2024, the data highlights a distinct split between fully remote and fully on-site roles, illustrating the continued prevalence and viability of remote work arrangements in the industry.
        """
    )

st.markdown("---")
st.markdown(
    """
    ### Data Source
    - **Dataset Name:** Data Developer Salary in 2024
    - **Source Link:** https://www.kaggle.com/datasets/shahzadi786/111111111111111111111
    - **Last Updated:** 2025-11-14
    - **Number of Rows:** 16534
    """
)
with st.expander("Data Preview"):
    st.dataframe(df)

utils.render_footer()

