import streamlit as st

st.title("S.T.O.P")
st.write("smartphone toxic overcome project")
st.markdown("---")
embed_code = """
<iframe title="project2_도입부 (1)" width="800" height="400" src="https://app.powerbi.com/view?r=eyJrIjoiMTMyZjY2OTQtM2ZmNC00MTIzLWFmOTEtMzZhNWE2MTEwZmY1IiwidCI6ImU0ZmVkY2NkLWRlOWMtNGUxMS04NDY3LWI0Y2FjMTliYzIzMyJ9" frameborder="0" allowFullScreen="true"></iframe>
"""
st.markdown(embed_code, unsafe_allow_html=True)

st.markdown("---")

st.page_link("pages/main.py", label="설문하러가기", icon="✔️")