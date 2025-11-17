import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

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
    st.subheader("1. Salary by experience level (box plots)")
    st.markdown(
        "**Question:** How does salary vary by experience level, and is there evidence of drop-offs or plateaus as experience increases?"
    )
    st.markdown(
        """
        **How to read this chart**
        - Each box shows the spread of salaries for one experience level (entry, mid, senior, executive).
        - The horizontal line inside each box is the median salary for that group.
        - The whiskers and dots show lower and higher salaries, including extreme values.
        - Compare the height and position of boxes to see which levels typically earn more.

        **What the data shows**
        - Median salaries increase as experience level rises from entry to senior/executive.
        - Senior and executive roles have much wider salary ranges, with some very high outliers.
        - Entry-level salaries are more tightly clustered, with fewer extreme high values.
        - There is some overlap between adjacent levels, but higher experience still shifts the whole box upward.
        """
    )

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

with row1_col2:
    st.subheader("2. Distribution of salaries (histogram)")
    st.markdown("**Question:** What does the overall distribution of salaries look like in this dataset?")
    st.markdown(
        """
        **How to read this chart**
        - The x‑axis shows salary ranges in US dollars.
        - The height of each bar shows how many records fall into that salary range.
        - The dashed vertical line marks the median salary.
        - Taller bars mean that salary range is more common.

        **What the data shows**
        - Most salaries cluster in a band well below the highest values in the dataset.
        - The distribution is right‑skewed: a long tail of high salaries with relatively few people.
        - The median salary sits to the left of the highest bars, reflecting the skew.
        - Very high salaries exist but are rare compared to the main body of the distribution.
        """
    )

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

row2_col1, row2_col2 = st.columns(2)

with row2_col1:
    st.subheader("3. Salary over time with median trend line")
    st.markdown(
        "**Question:** How has the typical (median) salary changed across the work years in this dataset?"
    )
    st.markdown(
        """
        **How to read this chart**
        - Each point on the line is the median salary for a given work year.
        - The x‑axis lists work years; the y‑axis shows median salary in US dollars.
        - The line connects yearly medians so you can see the trend over time.
        - Look at the slope of the line to see whether salaries are rising, falling, or flattening.

        **What the data shows**
        - Median salaries generally increase over the early years in the dataset.
        - The rate of increase appears to slow in the most recent years rather than rising sharply.
        - There is no sudden collapse in median salary; the pattern is gradual rather than volatile.
        - Overall, the trend suggests steady growth with hints of flattening toward the end of the period.
        """
    )

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

with row2_col2:
    st.subheader("4. Remote vs on-site roles in 2024")
    st.markdown(
        "**Question:** In 2024, how many roles are fully on‑site compared to fully remote?"
    )
    st.markdown(
        """
        **How to read this chart**
        - The x‑axis shows two categories: 0 (fully on‑site) and 100 (fully remote).
        - The height of each bar is the number of roles in that category for 2024.
        - Compare the bar heights to see which working arrangement is more common.
        - Hover over a bar to see the exact count.

        **What the data shows**
        - One working arrangement clearly has more roles than the other in 2024.
        - The difference between the two bars captures how prevalent fully remote work is versus fully on‑site work.
        - Even when one category dominates, the other still represents a meaningful portion of the dataset.
        - This simple comparison sets up deeper questions about how remote status connects to salary and role type.
        """
    )

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
st.markdown("---")
st.markdown("### Keep Exploring")

col_a, col_b, col_c, col_d = st.columns(4)

with col_a:
    st.page_link("Bio.py", icon="👤")

with col_b:
    st.page_link(
        "pages/1_EDA_Gallery.py",
        label="EDA Gallery",
        icon="🧪",
    )

with col_c:
    st.page_link(
        "pages/2_Dashboard.py",
        label="Dashboard",
        icon="📊",
    )

with col_d:
    st.page_link(
        "pages/3_Future_Work.py",
        label="Future Work",
        icon="🧭",
    )

st.markdown("---")
st.markdown(
    """
    <div style="text-align:center; color: #888; font-size: 0.85rem; padding: 0.5rem 0 1rem 0;">
        <p>© 2025 Ben Hislop · Built with Streamlit</p>
        Find me on:
        <a href="https://www.linkedin.com/in/benjaminhislop/" target="_blank">LinkedIn</a> | 
        <a href="https://github.com/Bphissles" target="_blank">GitHub</a> | 
        <a href="https://www.thejrtagency.com/" target="_blank">JRT Agency</a>
    </div>
    """,
    unsafe_allow_html=True,
)