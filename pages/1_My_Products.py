# My Producst
import streamlit as st

st.set_page_config(page_title="Products Recommend", page_icon="🧐")

st.markdown("# 🧐 Products Recommend")
st.sidebar.header("Products Recommend")

st.write("")
# 사용자 입력: 보유한 제품 선택
st.subheader("📌 보유한 제품을 선택하세요.")
user_products = st.multiselect(
    "내가 가지고 있는 제품",
    ["냉장고", "식기세척기", "정수기", "세탁기", "건조기", "로봇 청소기", "공기 청정기", "에어컨", "TV" ],
    default=[]
)

# 추천 제품 로직 (예제)
recommendations = {
    "냉장고": ["LG 디오스 오브제컬렉션 매직스페이스 냉장고", "LG 일반냉장고 오브제컬렉션", "LG 컨버터블 패키지 오브제컬렉션"],
    "식기세척기": ["LG 디오스 식기세척기", "LG 디오스 오브제컬렉션 식기세척기"],
    "정수기": ["LG 퓨리케어 정수기", "LG 퓨리케어 오브제컬렉션 정수기"],
    "세탁기": ["LG 통돌이 세탁기", "LG 트롬 오브제컬렉션 세탁기"],
    "로봇 청소기": ["LG 코드제로 A9 Air", "LG 코드제로 로보킹 AI 올인원", ],
    "공기 청정기": ["LG 퓨리케어 360˚ 공기청정기 Hit", "LG 퓨리케어 오브제컬렉션 에어로부스터", "LG 퓨리케어 오브제컬렉션 AI+ 360˚ 공기청정기"],
    "에어컨": ["LG 휘센 벽걸이에어컨", "LG 휘센 오브제컬렉션 뷰 에어컨 2in1"],
    "TV": ["LG 울트라 HD TV (스탠드형)", "LG 올레드 TV (벽걸이형)", "LG 스탠바이미 2"]
}
st.write("")

# 추천 결과 출력
st.subheader("🎯 추천 제품 리스트")

recommended_items = set()
for product in user_products:
    recommended_items.update(recommendations.get(product, []))

if recommended_items:
    st.write("✅ 다음 제품을 추천합니다:")
    for item in recommended_items:
        st.markdown(f"- **{item}**")
else:
    st.warning("보유한 제품을 선택하면 추천 제품이 표시됩니다!")
