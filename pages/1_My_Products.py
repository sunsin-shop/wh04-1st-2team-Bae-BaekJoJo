# My Producst
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Products Recommend", page_icon="🧐")

st.markdown("# 🧐 Products Recommend")
st.sidebar.header("Products Recommend")

# 사용자 입력: 보유한 제품 선택
st.subheader("📌 보유한 제품을 선택하세요.")
user_products = st.multiselect(
    "내가 가지고 있는 제품",
    ["냉장고", "식기세척기", "정수기", "세탁기", "건조기", "로봇 청소기", "공기 청정기", "에어컨", "TV"],
    default=[]
)

# 추천 제품 목록
recommendations = {
    "냉장고": ["LG 디오스 오브제컬렉션 매직스페이스 냉장고", "LG 일반냉장고 오브제컬렉션"],
    "식기세척기": ["LG 디오스 식기세척기", "LG 디오스 오브제컬렉션 식기세척기"],
    "정수기": ["LG 퓨리케어 정수기", "LG 퓨리케어 오브제컬렉션 정수기"],
    "세탁기": ["LG 통돌이 세탁기", "LG 트롬 오브제컬렉션 세탁기"],
    "로봇 청소기": ["LG 코드제로 A9 Air", "LG 코드제로 로보킹 AI 올인원"],
    "공기 청정기": ["LG 퓨리케어 360˚ 공기청정기", "LG 퓨리케어 오브제컬렉션 에어로부스터"],
    "에어컨": ["LG 휘센 벽걸이에어컨", "LG 휘센 오브제컬렉션 뷰 에어컨 2in1"],
    "TV": ["LG 울트라 HD TV", "LG 올레드 TV", "LG 스탠바이미 2"]
}

st.subheader("🎯 추천 제품 리스트")
recommended_items = set()
for product in user_products:
    recommended_items.update(recommendations.get(product, []))

if recommended_items:
    st.write("✅ 다음 제품을 추천합니다:")
    for item in recommended_items:
        st.markdown(f"- **{item}**")
    
    # 추가 기능: 사용자 맞춤 예산 입력 및 추천 제품 필터링
    st.subheader("💰 예산 입력")
    budget = st.number_input("최대 예산을 입력하세요 (만원)", min_value=0, step=10, value=100)
    
    # 가상의 가격 데이터 추가
    product_prices = {
        "LG 디오스 오브제컬렉션 매직스페이스 냉장고": 200,
        "LG 일반냉장고 오브제컬렉션": 150,
        "LG 디오스 식기세척기": 100,
        "LG 디오스 오브제컬렉션 식기세척기": 130,
        "LG 퓨리케어 정수기": 80,
        "LG 퓨리케어 오브제컬렉션 정수기": 90,
        "LG 통돌이 세탁기": 90,
        "LG 트롬 오브제컬렉션 세탁기": 140,
        "LG 코드제로 A9 Air": 70,
        "LG 코드제로 로보킹 AI 올인원": 120,
        "LG 퓨리케어 360˚ 공기청정기": 95,
        "LG 퓨리케어 오브제컬렉션 에어로부스터": 130,
        "LG 휘센 벽걸이에어컨": 85,
        "LG 휘센 오브제컬렉션 뷰 에어컨 2in1": 170,
        "LG 울트라 HD TV": 110,
        "LG 올레드 TV": 180,
        "LG 스탠바이미 2": 130
    }
    
    affordable_items = [item for item in recommended_items if product_prices.get(item, 999) <= budget]
    
    if affordable_items:
        st.subheader("💡 예산 내 추천 제품")
        for item in affordable_items:
            st.markdown(f"- **{item}** (가격: {product_prices[item]}만원)")
    else:
        st.warning("입력한 예산 내에서 추천할 수 있는 제품이 없습니다.")
else:
    st.warning("보유한 제품을 선택하면 추천 제품이 표시됩니다!")
