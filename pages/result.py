import streamlit as st

total_score = st.session_state.total_score
sex = st.session_state.sex
age = st.session_state.age


st.write('합계 : ',total_score)