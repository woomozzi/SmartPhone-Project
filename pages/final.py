import streamlit as st

st.title("마지막")
st.markdown("---")

embed_code = """
<iframe title="project2_마지막 페이지" width="800" height="400" src="https://app.powerbi.com/view?r=eyJrIjoiYTY2ZGMyNTItNjcwNi00NTAyLTkwNTktNmE4MGI2ZjFmNzhkIiwidCI6ImU0ZmVkY2NkLWRlOWMtNGUxMS04NDY3LWI0Y2FjMTliYzIzMyJ9" frameborder="0" allowFullScreen="true"></iframe>
"""
st.markdown(embed_code, unsafe_allow_html=True)

