import streamlit as st

st.set_page_config(
    page_title = "adult",
    page_icon = "👋"
)

st.title("adult")


questions_options = {
    "1. 새해 결심으로 스마트폰 사용을 줄이기로 결심했을때 결과가 어땠나요?": {
        1: "이용시간이 많이 줄었다.",
        2: "미미하지만 이용시간이  줄었다.",
        3: "한번도 성공 한 적이 없다.",
        4: "줄이기는 커녕 오히려 더 이용시간이 늘었다."
    },
    "2. 내일 당신은 아침 일찍 가족들과의 여행이 약속되어있습니다. 당신은 어떻게 할건가요?": {
        1: "완벽하게 준비를 해두고 내일 여행을 위해 일찍 잔다.",
        2: "스마트폰을 보다가 일찍 잔다.",
        3: "늦은시간까지 스마트폰을 보다가 잠든다.",
        4: "일찍 일어나야 하지만 새벽까지 스마트폰을 봐서 밤을 새버린다."
    },
    "3. 당신은 스마트폰 이용시간을 지키는것이 어려운가요?": {
        1: "전혀 그렇지 않다",
        2: "그렇지 않다",
        3: "그렇다",
        4: "매우 그렇다"
    },
    "4. 당신은 지금 내일까지 끝내야 하는 과제가 있습니다. 과제를 하던 중 당신이 좋아하는 유튜버의 영상이 업로드 됐다는 알림이 왔습니다. 당신은 어떻게 행동 할 건가요?": {
        1: "알림이 뜨던 말던 과제에 집중한다.",
        2: "과제를 마치고 본다.",
        3: "유튜버의 영상을 보다가 시간이 늦어서 과제를 급하게 한다.",
        4: "당장 과제를 접어두고 유튜버의 영상을 보다가 과제를 하지 못한다."
    },
    "5. 당신의 스마트폰이 고장나서 하루 동안 스마트폰을 쓸 수가 없습니다. 당신의 기분은 어떤가요?": {
        1: "스마트폰을 신경 쓰지 않고 다른 활동을 즐긴다.",
        2: "스마트폰 생각이 안 난다",
        3: "스마트폰 생각이 머리에서 떠나지 않는다.",
        4: "스마트폰이 너무 하고 싶어서 손이 떨리고, 불안하다"
    },
    "6. 당신의 스마트폰이 지정된 시간에 열리는 상자에 들어 있습니다. 당신은 어떻게 행동 할 것인가요?": {
        1: "스마트폰이 상자에 들어있다는 사실을 잊고 다른 활동을 즐긴다.",
        2: "열리기까지 기다린다.",
        3: "상자를 열 방법을 찾는다.",
        4: "상자를 부수고 스마트폰을 꺼내서 한다."
    },
    "7. 스마트폰 이용 때문에 건강에 문제가 생긴 적이 있나요?": {
        1: "건강에 이상이 없다.",
        2: "잘 모르겠다.",
        3: "건강이 나빠짐을 느꼈다.",
        4: "시력이 너무 나빠지고 , 자세가 뒤틀렸다."
    },
    "8. 스마트폰 이용 때문에 가족과 심하게 다툰 적이 있나요?": {
        1: "전혀 그렇지 않다",
        2: "그렇지 않다",
        3: "그렇다",
        4: "매우 그렇다"
    },
    "9. 친구나 회사생활에서 스마트폰을 자주 이용하여  친구들과 회사동료들과의 관계가 멀어진 적이 있나요?": {
        1: "문제가 될 만큼 이용하지 않는다.",
        2: "갈등이 생긴 적이 없다.",
        3: "사이가 서먹해졌다.",
        4: "친구관계와 사회적 관계가 망가졌다."
    },
    "10. 중요한 회의 중 스마트폰 알림이 계속해서 도착 할 때 당신은 어떻게 행동하나요?": {
        1: "회의에 집중 하기 위해 스마트폰을 두고 들어간다.",
        2: "회의에 집중한다.",
        3: "알림이 신경 쓰여서 회의에 집중이 흐트러진다.",
        4: "회의 중이지만 알림이 올 때 마다 스마트폰을 확인한다."
    }
}

# 사용자의 선택 저장할 딕셔너리
user_responses = {}

# 각 질문에 대해 반복
for question, options in questions_options.items():
    # 옵션 보여주고 사용자 선택
    selected_option_key = st.radio(question, list(options.keys()), format_func=lambda x: options[x] if x != list(options.keys()) else x)
    # 사용자가 선택한 옵션의 키를 딕셔너리에 저장
    user_responses[question] = selected_option_key

# 모든 질문에 대한 사용자의 선택 출력
st.write("선택한 옵션들:")
for question, key in user_responses.items():
    # 선택한 옵션의 키값과 해당 키에 대한 값을 출력
    st.write(f"{question}: {key}")