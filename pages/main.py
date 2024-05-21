import streamlit as st

st.set_page_config(
    page_title = "HOME",
    page_icon = "👋"
)

st.title("당신의 스마트폰 과의존 위험군을")
st.title("진단 해보세요📱")
st.markdown("---")

if 'total_score' not in st.session_state:
    st.session_state.total_score = 0

if 'total_score_adult' not in st.session_state:
    st.session_state.total_score_adult = 0

# 이름을 입력 받고 session_state에 저장
name = st.text_input('이름을 입력하세요! (자녀 진단시 자녀이름)')
st.session_state.name = name
sex = st.text_input('성별을 입력하세요! (남 / 여)')
st.session_state.sex = sex
age = st.text_input('나이를 입력하세요! (자녀 진단시 자녀나이)')
st.session_state.age = age
st.markdown("---")

st.subheader('👧 kids : 3-9세 자녀를 둔 부모')
st.page_link("pages/kids.py", label="kids", icon="✔️")
st.subheader('🧑‍🦰 adult : 10세 이상')
st.page_link("pages/adult.py", label="adult", icon="✔️")
