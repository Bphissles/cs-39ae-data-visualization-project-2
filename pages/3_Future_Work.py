import streamlit as st
import utils

st.set_page_config(
    page_title="Future Work | Professional Portfolio",
    page_icon="💎",
    layout="wide",
)

st.title("Future Work & Roadmap")
st.markdown(
    """
    Moving forward with this project, I plan to make changes to what the site does, and how it does it. 
    There are three main areas I plan to focus on:

    1. **Accessibility Audits:** Leveraging the accessibility tool [PowerMapper](https://www.powermapper.com/), 
    I'll be able to maintain WCAG compliance standards and ensure the site is accessible to all users.

    2. **Data Enrichment:** Integrating external datasets to provide additional context and insights. And create oppurtunities for
    exploring correlations between different datasets.

    3. **Machine Learning:** Integrating machine learning models to provide additional context and insights. And create oppurtunities for
    making predictions based on the data. Its nice to see where we've been, but its even more 
    interesting to see where we're going.

    4. **Under the Hood:** I plan to explore more functionality available in Streamlit. There are common components on the site that are being manually recreated,
    and I plan to explore the built-in components and how to use them.
    
    """
)

st.markdown("### Reflection")
st.markdown(
    """
    In developing the site, there were some observations I made, that changed direction of the project, from my [project plan](https://github.com/Bphissles/cs-39ae-data-visualization-project-2/blob/main/project-2.md). 
    - I planned on building a scatter plot with a trend line, but I realized after seeing it, that years were not a good candidate for a scatter plot. A more continuos date format could have worked but seeing is believing.
    - Building my project plan, I didn't plan for having an EDA showcase, and a Dashboard page, so I decided to integrate my research for my Machine Learning Project for additional visualizations.
    """
)

st.markdown("---")
utils.render_footer()

