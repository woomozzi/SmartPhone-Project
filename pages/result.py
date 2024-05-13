import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False


# ------------ 점수 변수 초기화 코드-------------
if 'total_score' not in st.session_state:
    st.session_state.total_score = 0

if 'total_score_adult' not in st.session_state:
    st.session_state.total_score_adult = 0
# ----------------------------------------------

# 변수 선언 코드
total_score = st.session_state.total_score
total_score_adult = st.session_state.total_score_adult
sex = st.session_state.sex
age = int(st.session_state.age)

# 점수 판별 함수
def overdose_kids(score) :
    if score >= 28:
       st.header('당신의 설문점수는 {}점 입니다.당신은 고위험군입니다. '.format(score))
    elif score >= 24 and score <= 27:
        st.header('당신의 설문점수는 {}점 입니다.당신은 잠재적위험군입니다.'.format(score))
    else :
        st.header('당신의 설문점수는 {}점 입니다.당신은 일반군입니다.'.format(score))

def overdose_adult_teen(score) :
    if score >= 31:
       st.header('당신의 설문점수는 {}점 입니다.당신은 고위험군입니다.'.format(score))
    elif score >= 23 and score <= 30:
        st.header('당신의 설문점수는 {}점 입니다.당신은 잠재적위험군입니다.'.format(score))
    else :
        st.header('당신의 설문점수는 {}점 입니다.당신은 일반군입니다.'.format(score))

def overdose_adult(score) :
    if score >= 29:
       st.header('당신의 설문점수는 {}점 입니다.당신은 고위험군입니다.'.format(score))
    elif score >= 24 and score <= 28:
        st.header('당신의 설문점수는 {}점 입니다.당신은 잠재적위험군입니다.'.format(score))
    else :
        st.header('당신의 설문점수는 {}점 입니다.당신은 일반군입니다.'.format(score))

def overdose_adult_senior(score) :
    if score >= 28:
       st.header('당신의 설문점수는 {}점 입니다.당신은 고위험군입니다.'.format(score))
    elif score >= 24 and score <= 27:
        st.header('당신의 설문점수는 {}점 입니다.당신은 잠재적위험군입니다.'.format(score))
    else :
        st.header('당신의 설문점수는 {}점 입니다.당신은 일반군입니다.'.format(score))

if total_score :
    overdose_kids(total_score)
else :
    if age >= 9 and age <= 24:
        overdose_adult_teen(total_score_adult)
    elif age > 24 and age < 60:
        overdose_adult(total_score_adult)
    elif age >= 60:
        overdose_adult_senior(total_score_adult)