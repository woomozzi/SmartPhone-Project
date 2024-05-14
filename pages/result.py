import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from powerbiclient import Report, models
from IPython.display import IFrame
from PIL import Image
import io
import openai 
import requests
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


client = openai.OpenAI(api_key = "secret")

# Call the API
# 1장 생성 시 0.03$ 
prompt = "나이가 " + str(age) + "살이고 스마트폰에 중독되어서 허리가 굽었고 다크서클이 턱까지 내려와서 폐인이 되어버린 " + sex + "자를 완전 무섭고 과장해서 그려줘"
response = client.images.generate(model="dall-e-3", prompt=prompt, size="1024x1024", quality="standard", n=1)

image_url = response.data[0].url

# 이미지를 가져와서 Streamlit에 표시
image = Image.open(requests.get(image_url, stream=True).raw)
st.image(image, caption='Generated Image', use_column_width=True)
