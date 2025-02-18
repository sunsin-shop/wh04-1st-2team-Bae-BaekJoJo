import pandas as pd
import streamlit as st

st.set_page_config(page_title="Outcall", page_icon="✔")
st.markdown("# Outcall")
st.sidebar.header("Outcall Page")

st.subheader("Select date")
dt_departures = st.date_input("출발일")

st.subheader("Select site")
province = {"서울특별시": 11, "부산광역시": 21, "대구광역시": 22, "인천광역시": 23, "광주광역시": 24, "대전광역시": 25, "울산광역시": 26, "세종특별자치시": 29, "경기도": 31, "강원도":32, "충청북도":  33, "충청남도": 34, "전라북도": 35, "전라남도": 36, "경상북도": 37, "경상남도": 38, "제주특별자치도": 39}

#province_name = st.text_input("메뉴 이름", placeholder="예: 서울특별시")
departures = st.selectbox(
    "출발지",
    options=list(province.keys()),
    #index=list(province.keys()).index('서울특별시')
)

#dt_arrivals = st.date_input("도착일")

arrivals = st.selectbox(
    "도착지",
    options=list(province.keys()),
    #index=list(province.keys()).index('부산광역시')
)


isPress = st.button("경로 설정")

if isPress:
    if departures and arrivals and dt_departures: #and dt_arrivals
        st.success(f"경로가 설정되었습니다.")
        st.success(f"📌{departures}📌에서 📌{arrivals}📌까지 현재 사용 가능한 교통수단은 아래와 같습니다.")
        #if insert_menu(menu_name, member_id, dt):
            #st.success(f"입력성공")
        #else:
            #st.error(f"입력실패")
    else:
        st.warning(f"모든 값을 입력해주세요!")