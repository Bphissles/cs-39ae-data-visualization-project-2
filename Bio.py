import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Ben Hislop | Professional Portfolio",
    page_icon="💎",
    layout="wide",
)

NAME = "Benjamin Hislop"
ROLE = "Full Stack Developer & AI Innovation Lead at the JRT agency "
SUMMARY = (
    "I am a full stack developer and AI innovation lead currently completing a Bachelor of Science in Computer Science. "
    "I balance full-time work, school, and being a parent to my 8-year-old son, so learning has become both a hobby and a priority. "
    "My interests include building pipeline tools that streamline workflows and build websites that service multiple B2B requirements. "
    "I enjoy the outdoors, hiking, skiing, and reading sci-fi novels."
)

PHOTO_PATH = Path(__file__).parent / "assets" / "headshot.jpeg"
ALT_TEXT = "Headshot of Benjamin Hislop"
# Alt text rendering issue: https://github.com/streamlit/streamlit/issues/8563

col1, col2 = st.columns([1, 2], vertical_alignment="center")

with col1:
    try:
        st.image(PHOTO_PATH, caption="Benjamin Hislop", width="stretch")
    except Exception as e:
        st.error(f"Could not load image: {e}")
        st.info(f"Looking for image at: {PHOTO_PATH}")

with col2:
    st.title(f"👋 {NAME}")
    st.subheader(ROLE)
    st.write(SUMMARY)

    st.markdown(
        """
        **Lets Talk:** [GitHub](https://github.com/Bphissles) | [LinkedIn](https://www.linkedin.com/in/benjaminhislop/)\n
        **Checkout my corporate work:** [the JRT agency](https://www.thejrtagency.com/)
        """
    )

col_left, col_right = st.columns(2)

with col_left:
    st.markdown(
        """
        ### Highlights
        - **Program**: Bachelor of Science in Computer Science at MSU Denver
        - **Tools**: Python, Pandas, Streamlit, Java 8, 11, and 17, Nuxt.js, PM2, Git, Jenkins, Docker
        - **Focus areas**: Data visualization, AI-assisted tooling, workflow automation, CMS development
        - **Interests**: AI education, AI tooling, Continuing Education, Business applications, Hiking
        """
    )

with col_right:
    st.markdown("### Visualization philosophy")
    st.write(
        """
        I see visualization as a bridge between complex systems and clear decisions. Charts should make it obvious what matters, 
        especially in B2B workflows where teams move quickly and context can be fragmented. I care about accessibility and 
        ethics in how data is presented - Avoiding dark, and anti-patterns, surfacing uncertainty when it matters, and pairing visuals with 
        clear communication that help people explore the story behind the numbers without getting lost in the noise.
        """
    )
st.markdown(
    """
### Project pages
Take a look at some of the work I've done during my time at MSU Denver below:
"""
)
col_a, col_b, col_c, col_d, col_e = st.columns(5)

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

with col_e:
    st.page_link(
        "pages/4_Network_Exploration.py",
        label="Network Exploration",
        icon="🕸️",
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