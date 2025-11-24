import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from anytree import Node, RenderTree
from networkx.algorithms.community import greedy_modularity_communities
import pandas as pd

st.set_page_config(
    page_title="Network Analysis | Friendship Graph",
    page_icon="🕸️",
    layout="wide",
)

st.title("Lab Exploration: Network Analysis")
st.divider()

G = nx.Graph()
G.add_edges_from([
    ("Alice","Bob"),("Alice","Charlie"),("Bob","Charlie"),("Charlie","Diana"),
    ("Diana","Eve"),("Bob","Diana"),("Frank","Eve"),("Eve","Ian"),
    ("Diana","Ian"),("Ian","Grace"),("Grace","Hannah"),("Hannah","Jack"),
    ("Grace","Jack"),("Charlie","Frank"),("Alice","Eve"),("Bob","Jack")
])

# Detailed Analysis Calculations 
degree = nx.degree_centrality(G)
betweenness = nx.betweenness_centrality(G)
closeness = nx.closeness_centrality(G)
eigenvector = nx.eigenvector_centrality(G, max_iter=1000)
df_metrics = pd.DataFrame({
    "Degree": pd.Series(degree),
    "Betweenness": pd.Series(betweenness),
    "Closeness": pd.Series(closeness),
    "Eigenvector": pd.Series(eigenvector),
}).sort_values("Degree", ascending=False)

# Community Detection Calculations
communities = greedy_modularity_communities(G)

# Community Visualization Calculations
st.header("Community Visualization")
st.markdown("""
\n
&nbsp;
\n
""")

palette = ["tab:blue", "tab:green", "tab:purple"]
node_to_comm = {}

for c_index, comm in enumerate(communities):
    for node in comm:
        node_to_comm[node] = c_index

community_colors = [palette[node_to_comm[n] % len(palette)] for n in G.nodes()]
pos = nx.spring_layout(G, seed=42) 

fig2, ax2 = plt.subplots(figsize=(10, 6))
nx.draw(
    G, pos, with_labels=True, node_size=3000,
    node_color=community_colors, edge_color="gray",
    font_size=8, font_weight="bold", 
    ax=ax2
)
ax2.set_title(
    "Friendship Network in a College Class",
    fontsize=22,
    fontweight='bold',
    verticalalignment='bottom',
    horizontalalignment='center',
)

col1, col2 = st.columns(2)

with col1:
  # --- Community Visualization ---
  st.pyplot(fig2)
  st.subheader("Friendship Observations")
  
  # Identify top nodes
  most_connected = df_metrics.index[0]
  most_influential = df_metrics.sort_values("Betweenness", ascending=False).index[0]
  
  st.markdown(f"""
  - **Most Connected:** {most_connected} (Highest Degree)
  - **Most Influential:** {most_influential} (Highest Betweenness)

  The network breaks into three tight groups, and Bob sits between them, bridging groups. If the need arose to quickly diseminate information, 
  Bob would be the fastest route for information. 
  """)

with col2:
# --- Community Detection ---
  st.header("Community Detection")
  st.dataframe(communities)
  # --- Detailed Analysis ---
  st.header("Detailed Analysis")
  st.dataframe(df_metrics, use_container_width=True)


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
