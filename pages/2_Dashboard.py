import streamlit as st
import pandas as pd
import plotly.express as px
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
    page_title="Student Performance Dashboard | Professional Portfolio",
    page_icon="💎",
    layout="wide",
)
st.title("Student Performance Factors")

data_path = Path(__file__).parent.parent / "data" / "student-dropout-risk.csv"

try:
    df = pd.read_csv(data_path, sep=";")
except Exception as e:
    st.error(f"Could not load data: {e}")
    st.info(f"Looking for data at: {data_path}")
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
    st.header("📊 Filter students")

    target_options = sorted(df["Target"].unique()) if "Target" in df.columns else []
    selected_targets = st.multiselect(
        "Outcome",
        options=target_options,
        default=[],
        help="Filter by final outcome (Graduate, Enrolled, Dropout)",
    )

    age_col = "Age at enrollment"
    if age_col in df.columns:
        min_age = int(df[age_col].min())
        max_age = int(df[age_col].max())
        selected_age_range = st.slider(
            "Age at enrollment",
            min_value=min_age,
            max_value=max_age,
            value=(min_age, max_age),
        )
    else:
        selected_age_range = None

df_filtered = df.copy()
if selected_targets:
    df_filtered = df_filtered[df_filtered["Target"].isin(selected_targets)]
if selected_age_range is not None:
    df_filtered = df_filtered[
        (df_filtered[age_col] >= selected_age_range[0])
        & (df_filtered[age_col] <= selected_age_range[1])
    ]

st.markdown(
    """
    Dashboard exploring how admission grades, course progress, and economic context relate to
    student outcomes (Graduate, Enrolled, Dropout). Data exploration originally performed during 
    initial data analysis for my Machine Learning final project.

    Follow the progress [here](https://www.benhislop.com/)
    """
)

st.divider()
# ROW 1: performance vs admission
col1_r1, col2_r1 = st.columns([2, 1])

with col1_r1:
    st.subheader("Admission grade vs first-semester performance")
    st.caption("Each point is a student; color shows final outcome.")

    for col in [
        "Admission grade",
        "Curricular units 1st sem (grade)",
    ]:
        if col not in df_filtered.columns:
            st.error(f"Expected column '{col}' not found in data.")
            st.stop()

    fig = px.scatter(
        df_filtered,
        x="Admission grade",
        y="Curricular units 1st sem (grade)",
        color="Target",
        opacity=0.5,
        labels={
            "Admission grade": "Admission grade",
            "Curricular units 1st sem (grade)": "1st-semester average grade",
            "Target": "Outcome",
        },
        title="Higher admission grades tend to align with stronger first-semester performance",
        color_discrete_sequence=[theme["primary"], theme["secondary"]],
    )
    fig.update_layout(legend_title_text="Outcome")
    st.plotly_chart(fig, use_container_width=True)

with col2_r1:
    st.subheader("How to read this dashboard")
    st.write(
        "This dashboard summarizes a student dropout-risk dataset. The first chart shows how "
        "admission grades relate to first-semester performance, broken down by final outcome. "
        "Use it to see whether higher starting preparation appears to protect against dropout."
    )

st.divider()
# ROW 2: heatmaps of course progress
col1_r2, col3_r2 = st.columns(2)

with col1_r2:
    st.subheader("1st-semester progress")
    st.caption("Relationship between enrolled and approved units in the 1st semester.")

    col_enrolled = "Curricular units 1st sem (enrolled)"
    col_approved = "Curricular units 1st sem (approved)"
    if col_enrolled in df_filtered.columns and col_approved in df_filtered.columns:
        fig = px.density_heatmap(
            df_filtered,
            x=col_enrolled,
            y=col_approved,
            nbinsx=10,
            nbinsy=10,
            labels={
                col_enrolled: "Units enrolled (1st sem)",
                col_approved: "Units approved (1st sem)",
            },
            title="Where students cluster by enrollment vs approvals",
            color_continuous_scale=theme["heatmap"],
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.error("Expected 1st-semester curricular unit columns not found in data.")

# with col2_r2:
#     st.subheader("Outcome mix by economic context")
#     st.caption("How outcomes vary across unemployment-rate bands.")

#     if "Unemployment rate" in df_filtered.columns and "Target" in df_filtered.columns:
#         df_bins = df_filtered.copy()
#         df_bins["Unemployment band"] = pd.cut(
#             df_bins["Unemployment rate"], bins=4, precision=1
#         )
#         counts = (
#             df_bins.groupby(["Unemployment band", "Target"])
#             .size()
#             .reset_index(name="count")
#         )
#         counts["Unemployment band"] = counts["Unemployment band"].astype(str)
#         fig = px.bar(
#             counts,
#             x="Unemployment band",
#             y="count",
#             color="Target",
#             labels={"count": "Number of students", "Unemployment band": "Unemployment rate band"},
#             title="Student outcomes across unemployment-rate bands",
#             color_discrete_sequence=[theme["primary"], theme["secondary"]],
#         )
#         fig.update_layout(xaxis_tickangle=-30)
#         st.plotly_chart(fig, use_container_width=True)
#     else:
#         st.error("Expected 'Unemployment rate' or 'Target' columns not found in data.")

with col3_r2:
    st.subheader("2nd-semester progress")
    st.caption("Relationship between enrolled and approved units in the 2nd semester.")

    col_enrolled_2 = "Curricular units 2nd sem (enrolled)"
    col_approved_2 = "Curricular units 2nd sem (approved)"
    if col_enrolled_2 in df_filtered.columns and col_approved_2 in df_filtered.columns:
        fig = px.density_heatmap(
            df_filtered,
            x=col_enrolled_2,
            y=col_approved_2,
            nbinsx=10,
            nbinsy=10,
            labels={
                col_enrolled_2: "Units enrolled (2nd sem)",
                col_approved_2: "Units approved (2nd sem)",
            },
            title="Where students cluster in the 2nd semester",
            color_continuous_scale=theme["heatmap"],
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.error("Expected 2nd-semester curricular unit columns not found in data.")

st.markdown("---")
st.markdown(
    """
    ### Data Source
    - **Dataset Name:** Predict Students' Dropout and Academic Success
    - **Source Link:** https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success
    - **Last Updated:** 12-12-2021
    - **Number of Rows:** 4424
    """
)
with st.expander("Data Preview"):
    st.dataframe(df)
st.markdown("---")
st.markdown(
    """
### Keep Exploring
"""
)
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