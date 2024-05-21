import streamlit as st
import os
def main():
    st.title("프로젝트 요약")

    # PDF 파일 경로
    pdf_path = "data/project2_포폴.pdf"

    # PDF 파일이 존재하는지 확인
    if not os.path.exists(pdf_path):
        st.error("PDF file not found.")
        return

    # PDF 파일을 iframe에 표시
    st.write(f'<iframe src="{pdf_path}" width="700" height="1000"></iframe>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()