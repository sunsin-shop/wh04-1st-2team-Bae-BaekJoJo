import streamlit as st

st.set_page_config(page_title="Music", page_icon="💜")
st.markdown("# Music 🎧🎶🎵")
st.sidebar.markdown("# Music 🎧🎶🎵")

genres = {"Kpop": 1, "Rock": 2, "Hip-Hop": 3, "Jazz": 4, "Classical": 5, "Electronic": 6, "R&B": 7, "Pop": 8, "Reggae": 9}

st.subheader("오늘의 mood")
today_mood = st.text_input("원하는 키워드를 입력해주세요.", placeholder="예: 즐거움, 슬픔 ... ")
music_genre = st.selectbox("원하는 장르를 선택해주세요.", options =  list(genres.keys()), index = list(genres.keys()).index('Kpop'))
music_num = st.slider("Pick a number", 0, 100)

isPress = st.button("오늘의 PLAYLIST📀 생성하기")

if isPress:
    if today_mood and music_num:
        st.success(f"{today_mood} 와 {music_genre} 을(를) 기반으로 #오늘의 PLAYLIST📀 {music_num}곡 생성 완료")
    else:
        st.warning(f"모든 값을 입력해주세요!")
        
st.subheader("오늘의 PLAYLIST📀")



isPress = st.button("오늘의 PLAYLIST📀 재생하기")
#st.audio()
if isPress:
    VIDEO_URL = "https://youtu.be/TtLXQ8wp7is?si=ebDXdFzGwrlNv1-F"
    st.video(VIDEO_URL)