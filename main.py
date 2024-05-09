import streamlit as st

st.set_page_config(
    page_title = "HOME",
    page_icon = "👋"
)

st.title("과의존 위험군?")

# 이름을 입력 받고 session_state에 저장
name = st.text_input('이름을 입력하세요!')
st.session_state.name = name
sex = st.text_input('성별을 입력하세요! (남, 여)')
st.session_state.sex = sex
age = st.text_input('나이를 입력하세요!')
st.session_state.age = age

st.subheader('👧 kids : 3-9세')
st.page_link("pages/kids.py", label="kids", icon="✔️")
st.subheader('🧑‍🦰 adult : 10세 이상')
st.page_link("pages/adult.py", label="adult", icon="✔️")
