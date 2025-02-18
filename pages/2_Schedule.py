import streamlit as st
import pandas as pd
import datetime
from datetime import date
from streamlit_calendar import calendar
import json

# 직원 index
emp_index = {"1": "조규민", "2": "김상득"}

# JSON 파일 읽기
def read_data(): 
    with open('src/schedule.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data
        
def make_df(data):  
    task_list = []
    for key, tasks in data.items():
        for task_key, task in tasks.items():
            task['id'] = key
            task['name'] = emp_index[key]
            task['task_name'] = task_key
            task_list.append(task)

    df = pd.DataFrame(task_list)
    return df

# 페이지 제목
st.title("📅 일정 캘린더")

# 일정 데이터 초기화
if "events" not in st.session_state:
    st.session_state["events"] = make_df(read_data())

# 일정 추가 폼
with st.form(key="event_form"):
    emp = st.selectbox("직원번호", ["1", "2"])
    title = st.text_input("일정 제목")
    start_date = st.date_input("시작일", datetime.date.today())
    start_date = start_date.strftime('%Y-%m-%d')
    end_date = st.date_input("종료일", datetime.date.today())
    end_date = end_date.strftime('%Y-%m-%d')
    submit_button = st.form_submit_button(label="일정 추가")

    if submit_button:
        data = read_data()
        task_number = len(data[emp])
        new_task_number = f"task{task_number + 1}"
        
        new_event = {
            "title": title,
            "start": start_date,
            "end": end_date
        }
        
        data[emp][new_task_number] = new_event
        
        with open('src/schedule.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        
        st.session_state["events"] = make_df(read_data())
        st.success(f"일정 '{title}'이(가) 추가되었습니다.")

# 캘린더 표시
st.subheader("📆 일정 보기")
calendar(events=st.session_state["events"].to_dict(orient="records"))

# 일정 목록 보기
st.subheader("📝 일정 목록")
st.dataframe(st.session_state["events"])

