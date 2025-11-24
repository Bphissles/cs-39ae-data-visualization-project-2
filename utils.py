import streamlit as st

def render_footer():
    st.markdown("---")
    st.markdown("### Keep Exploring")

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
