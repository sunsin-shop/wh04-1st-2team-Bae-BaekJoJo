import streamlit as st

st.set_page_config(page_title="Main", page_icon="🏠")
st.title("스마트 어시스턴트 홈 🎛️")
#st.image

st.write(" 🏠 **당신의 일상을 더욱 스마트하게!**")
st.write(" ")
st.write("**가전제품을 추천받고 신청하면 일정 관리를 통해 가장 빠른 경로로 고객님을 찾아갑니다!!**")
st.write("**feat.능률 상승 Playlist를 들으며~**")
st.write(" ")
st.write(" ")
st.write(" ")

st.markdown("##### 📌 보유한 가전제품을 선택하면 추천 가전제품을 알려드립니다.")
st.write("👉 가전제품 추천 페이지로 이동하려면 아래 버튼을 클릭하세요.")
if st.button("🔍 가전제품 추천 페이지로 이동"):
    st.switch_page("pages/1_My_Products.py")

st.write(" ")
st.markdown("##### 📅 일정을 효율적으로 관리하세요!")
st.write("👉 캘린더 페이지로 이동하려면 아래 버튼을 클릭하세요.")
if st.button("📅 캘린더 페이지로 이동"):
    st.switch_page("pages/2_Schedule.py")

st.write(" ")
st.markdown("##### 🛣️ 출장 날짜와 출,도착지를 입력하면 경로를 추천해드립니다.")
st.write("👉 경로 탐색 페이지로 이동하려면 아래 버튼을 클릭하세요.")
if st.button("🗺️ 경로 탐색 페이지로 이동"):
    st.switch_page("pages/3_Pathfinder Login.py")

st.write(" ")
st.markdown("##### 🎵 키워드를 입력하면 음악을 추천해드립니다.")
st.write("👉 음악 추천 페이지로 이동하려면 아래 버튼을 클릭하세요.")
if st.button("🎶 음악 추천 페이지로 이동"):
    st.switch_page("pages/5_music.py")


st.sidebar.markdown("# 배백조조🦢")

#st.sidebar.title("🔍 페이지 선택")
#page = st.sidebar.radio("이동할 페이지를 선택하세요", ["🏠 Main", "🧐 Products Recommend", "📅 Schedule", "✔ Outcall", "🎵 Music"])




st.markdown("---")
st.write("📌 **Made with ❤️ using Streamlit** | © 2025 Smart Assistant")