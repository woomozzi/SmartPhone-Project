import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import json
import os


st.title("마지막")
st.markdown("---")

embed_code = """
<iframe title="project2_마지막 페이지" width="800" height="400" src="https://app.powerbi.com/view?r=eyJrIjoiYTY2ZGMyNTItNjcwNi00NTAyLTkwNTktNmE4MGI2ZjFmNzhkIiwidCI6ImU0ZmVkY2NkLWRlOWMtNGUxMS04NDY3LWI0Y2FjMTliYzIzMyJ9" frameborder="0" allowFullScreen="true"></iframe>
"""
st.markdown(embed_code, unsafe_allow_html=True)

st.markdown("---")

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
# creds = ServiceAccountCredentials.from_json_keyfile_name("C:\WEBDEVELOP_0507\data\stop-423605-4544fb4199a8.json", scope)
creds = ServiceAccountCredentials.from_json_keyfile_dict(st.secrets["stop_json"], scope)
client = gspread.authorize(creds)

# Google Sheets 열기
sheet = client.open("stop").sheet1

st.subheader("댓글 시스템")

user_name = st.text_input("이름")
user_comment = st.text_area("댓글")

if st.button("댓글 제출"):
    if user_name and user_comment:
        # 시트에 새로운 행 추가
        sheet.append_row([user_name, user_comment])
        st.success("댓글이 성공적으로 제출되었습니다.")
    else:
        st.warning("모든 필드를 입력해주세요.")

st.subheader("댓글 목록")
# Google Sheets에서 데이터 가져오기
data = sheet.get_all_records()

if data:
    # DataFrame으로 변환
    df = pd.DataFrame(data)

    # 열 이름을 '이름'과 '댓글'로 변경
    df.columns = ['이름', '댓글']
    
    # 데이터프레임에서 댓글 목록 표시
    for index, row in df.iterrows():
        st.write(f"**{row['이름']}**: {row['댓글']}")
else:
    st.info("댓글이 아직 없습니다.")