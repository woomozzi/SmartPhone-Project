import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

# 시각화에 사용할 데이터 로드
df = pd.read_csv("data\wepdata.csv", encoding='cp949')

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


# --------------나이에 따른 위험군 분포 코드--------------------------

df_2 = df[(df['가구원_연령'] >= (age-3)) & (df['가구원_연령'] <= (age+3))]
df_2['성별'] = df_2['성별'].replace({1:'남', 2:'여'})
df_2 = df_2[df_2['성별'] == sex]
df_3 = pd.DataFrame(df_2['위험군'].value_counts())
df_4 = pd.DataFrame(df_2['설문합계'].value_counts())
df_5 = pd.DataFrame(df_2['14.여가시간 주요 활동-1순위'].value_counts().reset_index())
df_5 = df_5.loc[df_5['14.여가시간 주요 활동-1순위'] != 0.0]
df_5['14.여가시간 주요 활동-1순위'] = df_5['14.여가시간 주요 활동-1순위'].replace({1.0 : "문화예술 관람 및 참여",
                                                               2.0 : "스포츠 관람 및 참여",
                                                               3.0 : "취미, 오락 활동(쇼핑/외식 등)",
                                                               4.0 : "스마트폰 이용",
                                                               5.0 : "관광활동(자연명승 관람, 캠핑 등)",
                                                               6.0 : "휴식활동(TV시청, 산책 및 걷기 등)",
                                                               7.0 : "사회 및 기타활동(친구만남, 종교활동 등)",
                                                               8.0 : "기타"})

plt.rcParams.update({'font.size': 16})

fig, ax = plt.subplots(figsize=(18, 8))
ax.bar(df_4.index, df_4['count'])
# 그래프에 제목 추가
plt.title('당신의 나이와 비슷하고 성별이 {}인 사람들의 점수표'.format(sex))
# Matplotlib figure 객체를 Streamlit에 전달
st.pyplot(fig)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# 첫 번째 그래프: 파이 차트 (위험군 비율)
sizes = df_3['count']
labels = df_3.index
ax1.pie(sizes, labels=labels, autopct='%1.1f%%')
ax1.set_title('당신의 나이와 비슷하고 성별이 {}자인 사람들의 위험군 비율'.format(sex))

# 두 번째 그래프: 파이 차트 (여가시간 주요활동)
sizes = df_5['count']
labels = df_5['14.여가시간 주요 활동-1순위']
ax2.pie(sizes, labels=labels, autopct='%1.1f%%')
ax2.set_title('당신의 나이와 비슷하고 성별이 {}자인 사람들의 여가시간 주요활동'.format(sex))


plt.tight_layout()  # 각 그래프 간의 간격 조정
st.pyplot(fig)
# ----------------------------------------------------------------