import pandas as pd
import streamlit as st

st.set_page_config(page_title="Login", page_icon="✔")
st.markdown("# Login")
st.sidebar.header("Login Page")


# 사용자 정보 (딕셔너리 형태로 저장)
users = {
    "김상득": "rlatkdemr1234!",
    "user1": "김상득1234!"
}

# 로그인 함수
def login():
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in users and users[username] == password:
            st.success("로그인 성공!")
            st.session_state.username = username  # 세션 상태에 사용자 이름 저장
            st.session_state.logged_in = True  # 세션 상태에 로그인 여부 저장
            st.session_state.page = "Outcall"  # 이동할 페이지 정보 저장
            #st.experimental_rerun()
            return True
        else:
            st.error("아이디 또는 비밀번호가 일치하지 않습니다.")
            return False

# 로그인 화면
if login():
    # 로그인 성공 시 실행될 코드
    st.write("로그인 성공! 환영합니다!")

              
        #if insert_menu(menu_name, member_id, dt):
            #st.success(f"입력성공")
        #else:
            #st.error(f"입력실패")
    # else:
    # st.warning(f"모든 값을 입력해주세요!")   
# else:
#     st.write("로그인 실패")        
