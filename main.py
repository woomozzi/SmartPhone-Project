import streamlit as st

st.set_page_config(
    page_title = "HOME",
    page_icon = "👋"
)

st.title("메인화면")

st.page_link("pages/kids.py", label="kids", icon="🪪")
st.page_link("pages/adult.py", label="adult", icon="🪪")