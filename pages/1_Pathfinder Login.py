import pandas as pd
import streamlit as st
import requests

st.set_page_config(page_title="Login", page_icon="✔")
st.markdown("# Login")
st.sidebar.header("Login Page")

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "container_visible" not in st.session_state:
    st.session_state["container_visible"] = False

# # 사용자 정보 (딕셔너리 형태로 저장)
# db_users = {
#     "김상득": "rlatkdemr1234!",
#     "user1": "김상득1234!",
#     "admin": "0000"
# }

# 로그인 함수

username = st.text_input("Username")
password = st.text_input("Password", type="password")
    
if st.button("Login"):
    # 사용자 정보 JSON 파일 읽기
    # url = "https://raw.githubusercontent.com/nunininu/json-server-vercel/refs/heads/main/db.json"
    api = "https://json-nunininu.vercel.app/users"
        
    try:
        response = requests.get(f'{api}?username={username}')
        users = response.json()
        #users = data.get("users", []) # url 사용할 땐 "users" 타겟으로 가져와 하므로 필요함
            
            
            
        if len(users) == 0:
            st.error("아이디를 확인해 주세요")
                
        db_passwd = users[0]['password']
        if db_passwd == password:
                st.success("로그인 성공! 환영합니다!")
                st.session_state.username = username
                st.session_state.logged_in = True
                st.session_state.page = "Outcall"
                st.session_state["logged_in"] = True
                st.session_state["container_visible"] = True
        else:                 
            st.error("아이디 또는 비밀번호가 일치하지 않습니다.")

    except Exception as e:
        st.error(f"안돼 멍청아: {e}")  # 오류 메시지 표시
            

# 로그인 화면
if st.session_state["logged_in"] and st.session_state["container_visible"]:
    with st.container():

        st.write(" ")
        st.markdown("##### 📅 일정을 효율적으로 관리하세요!")
        st.write("👉 캘린더 페이지로 이동하려면 아래 버튼을 클릭하세요.")
        button1 = st.button("📅 캘린더 페이지로 이동")

        st.write(" ")
        st.markdown("##### 🛣️ 출장 날짜와 출,도착지를 입력하면 경로를 추천해드립니다.")
        st.write("👉 경로 탐색 페이지로 이동하려면 아래 버튼을 클릭하세요.")
        button2 = st.button("🗺️ 경로 탐색 페이지로 이동")

        st.markdown("##### 📌 보유한 가전제품을 선택하면 추천 가전제품을 알려드립니다.")
        st.write("👉 가전제품 추천 페이지로 이동하려면 아래 버튼을 클릭하세요.")
        button3 = st.button("🔍 가전제품 추천 페이지로 이동")

        st.write(" ")
        st.markdown("##### 🎵 키워드를 입력하면 음악을 추천해드립니다.")
        st.write("👉 음악 추천 페이지로 이동하려면 아래 버튼을 클릭하세요.")
        button4 = st.button("🎶 음악 추천 페이지로 이동")

        if button4:
            st.switch_page("pages/5_Music.py")
        if button1:
            st.switch_page("pages/2_Schedule.py")
        if button2:
            st.switch_page("pages/3_Pathfinder Settings.py")
        if button3:
            st.switch_page("pages/4_My_Products.py")

    
   

# 사용자 정보 (딕셔너리 형태로 저장)
# users = {
#     "김상득": "rlatkdemr1234!",
#     "user1": "김상득1234!",
#     "admin": "0000"
# }

# username = st.text_input("Username")
# password = st.text_input("Password", type="password")
# log_button = st.button('login')

# # 로그인 검증
# if log_button:
#     if username in users and users[username] == password:
#         st.success("로그인 성공! 환영합니다!")
#         st.session_state.username = username  # 세션 상태에 사용자 이름 저장
#         st.session_state.logged_in = True  # 세션 상태에 로그인 여부 저장
#         st.session_state.page = "Outcall"  # 이동할 페이지 정보 저장
#         st.session_state["logged_in"] = True
#         st.session_state["container_visible"] = True
#             #st.experimental_rerun()
#     else:
#         st.error("아이디 또는 비밀번호가 일치하지 않습니다.")

    
    
    

# if st.session_state["container_visible"] :
#     with info_table:
#         st.success("로그인 성공! 환영합니다!")
# else:
#     info_table.markdown('<div class="hidden-container"> </div>', unsafe_allow_html=True)
      


        #if insert_menu(menu_name, member_id, dt):
            #st.success(f"입력성공")
        #else:
            #st.error(f"입력실패")
    # else:
    # st.warning(f"모든 값을 입력해주세요!")   
# else:
#     st.write("로그인 실패")        
