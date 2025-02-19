import streamlit as st

st.set_page_config(page_title="Main", page_icon="🏠")
st.title("스마트 어시스턴트 홈 🎛️")
#st.image

st.write(" 🏠 **당신의 일상을 더욱 스마트하게!**")
st.write(" ")
st.write("**일정 관리와 경로 탐색을 통해 빠르고 효율적인 업무가 가능합니다!!**")
st.write("**feat.가전제품 자동 추천과 능률 상승 Playlist를 들으며~**")
st.write(" ")
st.write(" ")
st.write(" ")

st.write(" ")
st.markdown("##### 로그인 후 사용 가능합니다!")
st.write("👉 로그인 페이지로 이동하려면 아래 버튼을 클릭하세요.")
if st.button("🔐 로그인 페이지로 이동"):
    st.switch_page("pages/1_Pathfinder Login.py")




st.sidebar.markdown("# 배백조조🦢")

#st.sidebar.title("🔍 페이지 선택")
#page = st.sidebar.radio("이동할 페이지를 선택하세요", ["🏠 Main", "🧐 Products Recommend", "📅 Schedule", "✔ Outcall", "🎵 Music"])




st.markdown("---")
st.write("📌 **Made with ❤️ using Streamlit** | © 2025 Smart Assistant")