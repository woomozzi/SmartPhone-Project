import streamlit as st

st.title("스마트폰 과의존 위험군")
st.markdown("---")
embed_code = """
<iframe title="project2_intro" width="800" height="400" src="https://app.powerbi.com/view?r=eyJrIjoiZDk0NWJiZWUtM2U5NS00ZWM2LWI1NzktNGU2MDM2ZjkyZTIzIiwidCI6ImU0ZmVkY2NkLWRlOWMtNGUxMS04NDY3LWI0Y2FjMTliYzIzMyJ9" frameborder="0" allowFullScreen="true"></iframe>
"""
st.markdown(embed_code, unsafe_allow_html=True)

st.page_link("pages/main.py", label="설문하러가기~", icon="✔️")