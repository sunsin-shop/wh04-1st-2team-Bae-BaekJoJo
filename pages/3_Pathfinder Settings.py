import pandas as pd
import datetime
import streamlit as st

st.set_page_config(page_title="Settings", page_icon="✔")
st.markdown("# Settings")
st.sidebar.header("Settings Page")

if 'departures' not in st.session_state:
    st.session_state.departures = None
if 'arrivals' not in st.session_state:
    st.session_state.arrivals = None
if 'dt_departures' not in st.session_state:
    st.session_state.dt_departures = None 

province = {"서울특별시": 11, "부산광역시": 21, "대구광역시": 22, "인천광역시": 23, "광주광역시": 24, "대전광역시": 25, "울산광역시": 26, "세종특별자치시": 29, "경기도": 31, "강원도":32, "충청북도":  33, "충청남도": 34, "전라북도": 35, "전라남도": 36, "경상북도": 37, "경상남도": 38, "제주특별자치도": 39}

def calculate_duration(start_time, end_time):
            """소요시간을 계산하는 함수"""
            start = datetime.datetime.strptime(start_time, "%H:%M")
            end = datetime.datetime.strptime(end_time, "%H:%M")
            duration = end - start

            hours = duration.seconds // 3600
            minutes = (duration.seconds % 3600) // 60

            return f"{hours}시간 {minutes}분"

if st.session_state.get("logged_in", False):  # 로그인 여부 확인
    st.write(f"{st.session_state.username}님, 환영합니다!")

    st.subheader("DateTime")

    col1, col2 = st.columns(2)  # 두 개의 열로 나누기

    with col1:
        dt_departures = st.date_input("출발일", value=st.session_state.dt_departures or None)

    with col2:
        hour_options = [f"{i:02d}:00" for i in range(24)]  # 00시부터 23시까지 시간 옵션 생성
        selected_hour = st.selectbox("시간", hour_options)

    # datetime 객체 생성
    if dt_departures and selected_hour:
        departure_datetime = datetime.datetime.combine(dt_departures, datetime.time.fromisoformat(selected_hour))
        st.write("선택된 날짜와 시간:", departure_datetime)
    
    # st.subheader("Select date")
    # dt_departures = st.date_input("출발일", value=st.session_state.dt_departures or None)  # 초기값 설정
    
    st.subheader("Locations")    
    #province_name = st.text_input("메뉴 이름", placeholder="예: 서울특별시")
    departures = st.selectbox(
    "출발지",
        options=list(province.keys()),
        index=list(province.keys()).index(st.session_state.departures) if st.session_state.departures in province else 0  # 초기값 설정 및 오류 방지
        )

    #dt_arrivals = st.date_input("도착일")
    arrivals = st.selectbox(
        "도착지",
        options=list(province.keys()),
        index=list(province.keys()).index(st.session_state.arrivals) if st.session_state.arrivals in province else 0 # 초기값 설정
        )
    
    st.session_state.departures = departures # 세션 상태 업데이트
    st.session_state.arrivals = arrivals # 세션 상태 업데이트
    st.session_state.dt_departures = dt_departures # 세션 상태 업데이트

    
    isPress = st.button("경로 안내")

    if isPress:
        if departures and arrivals and dt_departures: #and dt_arrivals
            st.success(f"📌{departures} 에서 📌{arrivals} 까지 {departure_datetime} 기준으로 사용 가능한 교통수단은 아래와 같습니다.")

            # 딕셔너리 형태로 데이터 구성
            table_data = {
                "교통수단": ["KTX", "기차", "버스"],
                "출발시각": ["16:02", "17:30", "18:45"],
                "도착시각": ["19:20", "20:50", "22:15"],
                "좌석수": [30, 50, 100],
                "예매하기": ["예매하기"] * 3  # "예매하기" 버튼 3개 생성
            }

            # 데이터프레임 생성
            df = pd.DataFrame(table_data)

            
            # "소요시간" 열 추가
            df["소요시간"] = df.apply(lambda row: calculate_duration(row["출발시각"], row["도착시각"]), axis=1)

            # # "예매" 열에 버튼 추가
            # df["예매하기"] = df.apply(lambda row: st.button("예매하기", key=f"btn_{row.name}"), axis=1)
            
            # # 버튼 클릭 처리 (추가)
            # for index, row in df.iterrows():
            #     if row["예매하기"]:
            #         st.write(f"{index}번 행의 예매하기 버튼이 클릭되었습니다.")
            
            # 각 버튼에 고유한 key 할당 및 클릭 처리
                        
            for index, row in df.iterrows():
                button_key = f"btn_{index}"

                # Check if the button was clicked in the *previous* run
                if button_key in st.session_state and st.session_state[button_key]:
                    st.write(f"{index}번 행의 예매하기 버튼이 클릭되었습니다.")
                    # ... (예약 처리 로직)

                    # Reset the button's state in st.session_state for the *next* run
                    st.session_state[button_key] = False  # Reset for the next click
                    st.experimental_rerun() # Rerun to reflect the reset immediately.
                    break # Stop after the first click is handled.

                # Display the button. The *return value* of st.button is ignored.
                st.button("예매하기", key=button_key)

            st.table(df)
            
            
            
            
            # for index, row in df.iterrows():
            #     button_key = f"btn_{index}"
            #     if button_key not in st.session_state:
            #         st.session_state[button_key] = False  # 초기 상태 설정

            #     if st.button("예매하기", key=button_key):
            #         st.session_state[button_key] = True  # 클릭 상태 업데이트
            #         buttons.append(True)  # 클릭된 버튼 저장
            #     else:
            #         buttons.append(False)

            # df["예매하기"] = buttons  # 데이터프레임에 버튼 상태 저장

            # st.table(df)

            # # 버튼 클릭 처리 (추가)
            # for index, row in df.iterrows():
            #     if row["예매하기"]:
            #         st.write(f"{index}번 행의 예매하기 버튼이 클릭되었습니다.")  # 예시: 어떤 버튼이 클릭되었는지 확인
            #         # 여기에 예매 처리 로직 추가
            #         st.session_state[f"btn_{index}"] = False # 클릭 후 상태 초기화
            #         break  # 첫 번째 클릭만 처리 (필요에 따라 수정)
            
            
            # # 테이블 출력
            # st.table(df)

        else:
            st.write("경로 설정 버튼을 눌러주세요.")   
            
                           
            #if insert_menu(menu_name, member_id, dt):
                #st.success(f"입력성공")
            #else:
                #st.error(f"입력실패")
        # else:
        # st.warning(f"모든 값을 입력해주세요!")   
        
else:
    st.write("로그인 후 이용해주세요")        
