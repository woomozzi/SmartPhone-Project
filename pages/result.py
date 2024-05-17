import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from powerbiclient import Report, models
from IPython.display import IFrame
from PIL import Image
import io
import openai 
import requests
import os



# ------------ 점수 변수 초기화 코드-------------

if 'total_score' not in st.session_state:
    st.session_state.total_score = 0

if 'total_score_adult' not in st.session_state:
    st.session_state.total_score_adult = 0

# --------------------변수 선언 코드-----------------

total_score = st.session_state.total_score
total_score_adult = st.session_state.total_score_adult
sex = st.session_state.sex
age = int(st.session_state.age)
name = st.session_state.name
# ----------------점수 판별 함수----------------------------------------

def overdose_kids(score) :
    if score >= 28:
       st.header('{}(이)는 고위험군으로 판정되었습니다! 😢'.format(name))
       st.header('설문점수는 {}점 입니다.'.format(score))
       st.markdown("---")
    elif score >= 24 and score <= 27:
        st.header('{}(이)는 잠재적위험군으로 판정되었습니다! 😶'.format(name))
        st.header('설문점수는 {}점 입니다.'.format(score))
        st.markdown("---")
    else :
        st.header('{}(이)는 일반군으로 판정되었습니다! 😎'.format(name))
        st.header('설문점수는 {}점 입니다.'.format(score))
        st.markdown("---")

def overdose_adult_teen(score) :
    if score >= 31:
       st.header('당신은 고위험군으로 판정되었습니다! 😢')
       st.header('설문점수는 {}점 입니다.'.format(score))
       st.markdown("---")
    elif score >= 23 and score <= 30:
        st.header('당신은 잠재적위험군으로 판정되었습니다! 😶')
        st.header('설문점수는 {}점 입니다.'.format(score))
        st.markdown("---")
    else :
        st.header('당신은 일반군으로 판정되었습니다! 😎')
        st.header('설문점수는 {}점 입니다.'.format(score))
        st.markdown("---")

def overdose_adult(score) :
    if score >= 29:
       st.header('당신은 고위험군으로 판정되었습니다! 😢')
       st.header('설문점수는 {}점 입니다.'.format(score))
       st.markdown("---")
    elif score >= 24 and score <= 28:
        st.header('당신은 잠재적위험군으로 판정되었습니다! 😶')
        st.header('설문점수는 {}점 입니다.'.format(score))
        st.markdown("---")
    else :
        st.header('당신은 일반군으로 판정되었습니다! 😎')
        st.header('설문점수는 {}점 입니다.'.format(score))
        st.markdown("---")

def overdose_adult_senior(score) :
    if score >= 28:
       st.header('당신은 고위험군으로 판정되었습니다! 😢')
       st.header('설문점수는 {}점 입니다.'.format(score))
       st.markdown("---")
    elif score >= 24 and score <= 27:
        st.header('당신은 잠재적위험군으로 판정되었습니다! 😶')
        st.header('설문점수는 {}점 입니다.'.format(score))
        st.markdown("---")
    else :
        st.header('당신은 일반군으로 판정되었습니다! 😎')
        st.header('설문점수는 {}점 입니다.'.format(score))
        st.markdown("---")

# ----------------대시보드 함수-------------------------------------------------

def dash_kids():
    embed_code = """
<iframe title="project2_유아동_결과" width="800" height="400" src="https://app.powerbi.com/view?r=eyJrIjoiMzIwNzFiYTctYzdlNy00YmExLTgyZGUtMGJhMjdiZWIzMTgwIiwidCI6ImU0ZmVkY2NkLWRlOWMtNGUxMS04NDY3LWI0Y2FjMTliYzIzMyJ9" frameborder="0" allowFullScreen="true"></iframe>
"""
    st.subheader('[ 자녀의 나이인 {}세가 포함된 구간의 설문조사 현황 ]'.format(age))
    st.markdown(embed_code, unsafe_allow_html=True)
def dash_adult_teens():
    embed_code = """
<iframe title="project2_청소년_결과" width="800" height="400" src="https://app.powerbi.com/view?r=eyJrIjoiMzA5YmQ4ZTAtZTNkOC00NzllLWEzNGEtOTI2ZDA3NjVmYmJjIiwidCI6ImU0ZmVkY2NkLWRlOWMtNGUxMS04NDY3LWI0Y2FjMTliYzIzMyJ9" frameborder="0" allowFullScreen="true"></iframe>
"""
    st.subheader('[ 당신의 나이인 {}세가 포함된 구간의 설문조사 현황 ]'.format(age))
    st.markdown(embed_code, unsafe_allow_html=True)
def dash_adult():
    embed_code = """
<iframe title="project2_성인_결과" width="800" height="400" src="https://app.powerbi.com/view?r=eyJrIjoiZWNmMmYyNmMtNmYzMC00NWVlLThhZDgtNWM0N2E1OGE4ODU3IiwidCI6ImU0ZmVkY2NkLWRlOWMtNGUxMS04NDY3LWI0Y2FjMTliYzIzMyJ9" frameborder="0" allowFullScreen="true"></iframe>
"""
    st.subheader('[ 당신의 나이인 {}세가 포함된 구간의 설문조사 현황 ]'.format(age))
    st.markdown(embed_code, unsafe_allow_html=True)
def dash_adult_senior():
    embed_code = """
<iframe title="project2_60대_결과" width="800" height="400" src="https://app.powerbi.com/view?r=eyJrIjoiYmQ1MTQ1MmMtYzllNC00NDA1LWE4YmItMTVkMjUyMjg4OTg5IiwidCI6ImU0ZmVkY2NkLWRlOWMtNGUxMS04NDY3LWI0Y2FjMTliYzIzMyJ9" frameborder="0" allowFullScreen="true"></iframe>
"""
    st.subheader('[ 당신의 나이인 {}세가 포함된 구간의 설문조사 현황 ]'.format(age))
    st.markdown(embed_code, unsafe_allow_html=True)

#----------------------------------솔루션 함수--------------------------------------

def solution_kids_overdose():
    st.markdown("---")
    st.subheader("""
스마트폰 중독에는 여러가지 이유가 있지만 자녀의 스마트폰 이용 횟수와 시간을 제한할 것을 추천드립니다.\n
그럼 스마트폰 과의존에서 멀어질 수 있을 것입니다.\n
다음은 참고하실 수 있는 방법 몇가지를 알려드리겠습니다. 도움이 되었으면 좋겠습니다 !!
              """)
    st.markdown("---")
    st.subheader('스마트폰 과의존 현상이 유아들의 발달에 미치는 부정적인 영향')
    st.write("""
1. 창의적능력이 떨어지고, 인지 발달 측면에서 유아가 스마트폰을 과도하게 이용한 경우 주의집중력 저하 현상이 나타난다.\n
2. 유아기에 스마트폰 게임 과몰입을 하게되면 친사회적 행동의 발달과 문제행동에 대한 이해에 부정적영향을 미칠 수 있다.\n
    또한, 자기조절 능력과 공감능력이 낮아지고 감정조절과 충동억제가 힘들어지며 자기존중감에 부정적 영향을 미치게 된다.\n
3. 스마트폰 과의존이 심해지면 우울,불안 등의 정신적인 문제도 일으킬 수 있다.\n
4. 스마트 기기의 터치 및 모션의 제한적 사용으로 인해 시각외의 소근육 사용이 줄어들어 신체적 성장에 부정적인 영향을 미칠 수 있다.""")
    st.subheader('부모가 할 수 있는 예방법')
    st.write("""
1. 자녀에게 스마트폰 사용방법을 가르친다.\n
2. 자녀의 스마트폰 사용시간을 제한한다.\n
3. 자녀에게 스마트폰 사용의 좋은점과 나쁜점을 말해준다.\n
4. 자녀가 사용할 수 있는 특정한 스마트폰 앱이나 사이트(성인사이트등)를 제한한다.
             """)
    st.subheader('솔루션')
    st.write('1. 사용횟수 제한🚨: 주당 1~2회로 제한하여야 과의존 위험이 감소한다.\n 2. 유아의 사용시간 제한👶: 유아의 1회 평균 스마트폰 사용시간을 20분 이내로 제한하여야 과의존 위험이 감소한다.\n 3. 부모의 사용시간 제한🤱: 부모의 스마트폰 사용시간을 조절하여 유아의 과의존을 예방해야한다.')
    
def solution_kids_normal():
    st.markdown("---")
    st.subheader("""
이는 스마트폰 사용에 있어 균형 잡힌 생활을 하고 있다는 것을 의미합니다.\n
앞으로도 현재의 상태를 잘 유지하여 과의존 위험군이 되지 않도록 주의해 주세요.\n
스마트폰 사용을 적절히 조절하며 건강한 디지털 라이프를 이어가시길 바랍니다 😊
               """)
    st.markdown("---")
    st.subheader('스마트폰 과의존 현상이 유아들의 발달에 미치는 부정적인 영향')
    st.write("""
1. 창의적능력이 떨어지고, 인지 발달 측면에서 유아가 스마트폰을 과도하게 이용한 경우 주의집중력 저하 현상이 나타난다.\n
2. 유아기에 스마트폰 게임 과몰입을 하게되면 친사회적 행동의 발달과 문제행동에 대한 이해에 부정적영향을 미칠 수 있다.\n
    또한, 자기조절 능력과 공감능력이 낮아지고 감정조절과 충동억제가 힘들어지며 자기존중감에 부정적 영향을 미치게 된다.\n
3. 스마트폰 과의존이 심해지면 우울,불안 등의 정신적인 문제도 일으킬 수 있다.\n
4. 스마트 기기의 터치 및 모션의 제한적 사용으로 인해 시각외의 소근육 사용이 줄어들어 신체적 성장에 부정적인 영향을 미칠 수 있다.""")
    st.subheader('부모가 할 수 있는 예방법')
    st.write("""
1. 자녀에게 스마트폰 사용방법을 가르친다.\n
2. 자녀의 스마트폰 사용시간을 제한한다.\n
3. 자녀에게 스마트폰 사용의 좋은점과 나쁜점을 말해준다.\n
4. 자녀가 사용할 수 있는 특정한 스마트폰 앱이나 사이트(성인사이트등)를 제한한다.
             """)
def solution_adult_teens_overdose():
    st.markdown("---")
    st.subheader("""
청소년기는 가장 과의존 위험에 취약한 연령대로 더욱 더 주의가 필요합니다.\n
스마트폰 중독에는 여러가지 이유가 있지만 스마트폰 사용 시간을 조절하고 취미나 운동을 시작해보는 것을 추천드립니다.\n
그럼 스마트폰 과의존에서 멀어질 수 있을 것입니다.\n 
다음은 참고하실 수 있는 방법 몇가지를 알려드리겠습니다. 도움이 되었으면 좋겠습니다!!
              """)
    st.markdown("---")
    st.subheader('예방법')
    st.write("""
1. 스마트폰 사용방법을 배운다.\n
2. 스마트폰 사용의 좋은점과 나쁜점을 알아본다.\n
3. 함께 가족의 스마트폰 사용규칙을 만들고 다같이 지키려고 노력한다.\n
4. 유익한 사이트나 앱을 같이 사용한다.
             """)
    st.subheader('솔루션')
    st.write("""
1. 사용시간 조절⏰: 무조건적인 사용금지 보다 사용시간 조절이 필요하다.\n(자신에게 적절한 스마트폰 사용시간을 미리 정해 지키는 습관 + 일정시간만 스마트폰을 사용할 수 있도록 설정하는 앱 활용)
2. 외부활동 즐기기🏃‍♂️: 스마트폰 사용시간을 줄이고 친구들과 서로 어울려 사회성을 높일 수 있는 취미나 운동을 시작한다.\n
3. 자기통제력 기르기🧘: 명확한 목표설정, 적절한 보상, 긍정적 자아대화 등을 통해 자기통제력 기른다.
             """)
    
def solution_adult_teens_normal():
    st.markdown("---")
    st.subheader("""
이는 스마트폰 사용에 있어 균형 잡힌 생활을 하고 있다는 것을 의미합니다.\n                    
하지만 청소년기는 가장 과의존 위험에 취약한 연령대이므로\n
앞으로도 현재의 상태를 잘 유지하여 과의존 위험군이 되지 않도록 주의해 주세요.\n
스마트폰 사용을 적절히 조절하며 건강한 디지털 라이프를 이어가시길바랍니다😊
              """)
    st.subheader('예방법')
    st.write("""
1. 스마트폰 사용방법을 배운다.\n
2. 스마트폰 사용의 좋은점과 나쁜점을 알아본다.\n
3. 함께 가족의 스마트폰 사용규칙을 만들고 다같이 지키려고 노력한다.\n
4. 유익한 사이트나 앱을 같이 사용한다.
             """)
def solution_adult_overdose():
    st.markdown("---")
    st.subheader("""
스마트폰 중독에는 여러가지 이유가 있지만 사회관계에서 받는 스트레스를 줄이고,\n 
취미나 운동을 통해서 스트레스를 해소 해보는것을 추천드립니다.\n
그럼 스마트폰 과의존에서 멀어질 수 있을 것입니다.\n
다음은 참고하실 수 있는 방법 몇가지를 알려드리겠습니다.\n
도움이 되었으면 좋겠습니다!!
              """)
    st.subheader('솔루션')
    st.write("""
1. 의식적인 스마트폰 사용⏰: 스마트폰 사용 시간을 의식적으로 관리하고 제한하는 것이 중요하다. 사용하는 앱이나 기능에 대해 자주 질문해 보면서 자신이 얼마나 많은 시간을 소비하고 있는지를 파악한다.\n
2. 보상 체계 재조정🧗‍♂️: 스마트폰 사용에 따른 보상을 다른 방식으로 대체할 수 있는 방법을 찾아본다. 예를 들어, 취미나 운동과 같은 활동을 통해 보상을 받을 수 있도록 해본다.\n
3. 감정 관리👌: 부정적인 감정을 회피하지 않고 직면하고 처리할 수 있는 기술을 향상시킨다. 스트레스 관리 기술을 익히고, 감정을 표현하고 이해하는 방법을 배우는 것이 도움이 될 수 있다.\n
4. 자기 조절력 강화🧘: 스스로에 대한 자기 조절력을 강화하기 위해 명확한 목표를 설정하고 그 목표를 달성하기 위한 계획을 세운다. 이를 통해 자기 조절력을 연습하고 강화할 수 있다.\n
5. 취미나 운동🏃‍♂️: 평소 관심이 있는 분야나 해보고 싶었던 활동을 시작하면서 건강한 하루를 보내본다.\n
6. 심리적 지원 받기👨‍⚕️: 부정적인 감정이나 자기 조절이 어려울 때는 전문가의 도움을 받아본다. 심리상담이나 행동 치료를 통해 문제를 해결할 수 있다.

             """)
def solution_adult_normal():
    st.markdown("---")
    st.subheader("""
이는 스마트폰 사용에 있어 균형 잡힌 생활을 하고 있다는 것을 의미합니다.\n 
앞으로도 현재의 상태를 잘 유지하여 과의존 위험군이 되지 않도록 주의해 주세요.\n 
스마트폰 사용을 적절히 조절하며 건강한 디지털 라이프를 이어가시길 바랍니다 😊
              """)
def solution_adult_senior_overdose():
    st.markdown("---")
    st.subheader("""
스마트폰 중독에는 여러가지 이유가 있지만, 우울감과 무력감이 증가하기 때문에 그럴 수 있습니다.\n
새로운 경험과 도전을 시도해 보는것을 추천드립니다.\n
그럼 스마트폰 과의존에서 멀어질 수 있을 것입니다.\n 
다음은 참고하실 수 있는 방법 몇가지를 알려드리겠습니다. 도움이 되었으면 좋겠습니다 !!
              """)
    st.subheader('솔루션')
    st.write("""
1. 운동하기🏃‍♂️: 운동은 우울감을 줄이고 에너지를 회복하는데 도움이 된다. 산책, 조깅, 수영, 요가 등의 유산소 운동이나 근력 운동을 통해 신체 활동을 즐기고 건강을 유지한다.\n
2. 정기적인 활동👨‍👩‍👧‍👦: 정기적으로 계획된 활동을 가지고 생활하면 무기력감을 극복할 수 있다. 예를 들어, 취미활동이나 동호회 참여, 봉사활동 등을 통해 자신을 활발하게 유지한다.\n
3. 사회적 교류🗣️: 친구나 가족과의 만남이나 사회적인 활동을 통해 우울감을 줄일 수 있다. 사랑과 지지를 받으면서 대화하고 나눔을 통해 긍정적인 정서를 유지한다.\n
4. 정서적 지원👨‍⚕️: 우울감과 무기력감을 해소하기 위해 전문가의 도움을 받을 수 있다. 정신건강 전문가와의 상담이나 치료를 통해 문제에 대한 해결책을 찾을 수 있다.\n
5. 자기 관리😴: 충분한 휴식과 수면을 취하고 건강한 식습관을 유지한다. 스트레스를 관리하고 긍정적인 생각을 유지하는 것이 중요하다.\n
6. 새로운 경험과 도전🧗‍♂️: 새로운 취미나 활동을 시작하거나 도전적인 목표를 세우는 것은 자신감을 키우고 우울감을 극복하는 데 도움이 된다.\n
7. 커뮤니티 센터 프로그램🏫: 지역 사회에서 운영하는 다양한 프로그램에 참여하여 새로운 사람들과 교류할 수 있다. 이는 고립감을 줄이고 사회적 유대를 강화하는 데 도움을 준다.
             """)
def solution_adult_senior_normal():
    st.markdown("---")
    st.subheader("""
스마트폰 사용에 있어 균형 잡힌 생활을 하고 있다는 것을 의미합니다.\n
앞으로도 현재의 상태를 잘 유지하여 과의존 위험군이 되지 않도록 주의해 주세요.\n 
스마트폰 사용을 적절히 조절하며, 건강한 디지털 라이프를 이어가시길 바랍니다 😊
              """)

# ---------------------------------출력 코드-----------------------------------------  

if 'total_score' not in st.session_state:
    st.session_state.total_score = 0

if 'total_score_adult' not in st.session_state:
    st.session_state.total_score_adult = 0

if total_score :
    overdose_kids(total_score)
    dash_kids()
else :
    if age >= 9 and age <= 24:
        overdose_adult_teen(total_score_adult)
        dash_adult_teens()
    elif age > 24 and age < 60:
        overdose_adult(total_score_adult)
        dash_adult()
    elif age >= 60:
        overdose_adult_senior(total_score_adult)
        dash_adult_senior()


#------------------------------- ai 이미지 출력 코드----------------------------------------
# client = openai_api_key = st.secrets["openapi_key"]["OPENAPI_KEY"]

# if total_score >= 24:  # 과의존 위험군인 경우에만 이미지 생성
#     prompt = "나이가 " + str(age) + "살이고 스마트폰에 중독되어서 허리가 굽었고 다크서클이 턱까지 내려와서 폐인이 되어버린 " + sex + "자를 완전 무섭고 과장해서 그려줘"
#     response = client.images.generate(model="dall-e-3", prompt=prompt, size="1024x1024", quality="standard", n=1)

#     image_url = response.data[0].url

#     # 이미지를 가져와서 Streamlit에 표시
#     image = Image.open(requests.get(image_url, stream=True).raw)
#     st.subheader('당신의 미래모습..')
#     st.image(image, caption='Generated Image', use_column_width=True)

# if total_score_adult >= 24:  # 과의존 위험군인 경우에만 이미지 생성
#     prompt = "나이가 " + str(age) + "살이고 스마트폰에 중독되어서 허리가 굽었고 다크서클이 턱까지 내려와서 폐인이 되어버린 " + sex + "자를 완전 무섭고 과장해서 그려줘"
#     response = client.images.generate(model="dall-e-3", prompt=prompt, size="1024x1024", quality="standard", n=1)

#     image_url = response.data[0].url

#     # 이미지를 가져와서 Streamlit에 표시
#     image = Image.open(requests.get(image_url, stream=True).raw)
#     st.subheader('당신의 미래모습..')
#     st.image(image, caption='Generated Image', use_column_width=True)

if total_score :
    if total_score >= 24:
        solution_kids_overdose()
    elif total_score < 24:
        solution_kids_normal()
else :
    if (age > 9 and age <= 19) and (total_score_adult >= 23):
        solution_adult_teens_overdose()
    elif (age > 9 and age <= 19) and (total_score_adult < 23):
        solution_adult_teens_normal()
    elif (age > 24 and age < 60) and (total_score_adult >= 24):
        solution_adult_overdose()
    elif (age > 24 and age < 60) and (total_score_adult < 24):
        solution_adult_normal()
    elif (age > 60) and (total_score_adult >= 24):
        solution_adult_senior_overdose()
    elif (age > 60) and (total_score_adult < 24):
        solution_adult_senior_normal()
st.markdown("---")
st.page_link("pages/final.py", label="마지막가기", icon="✔️")
