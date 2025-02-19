# Customer information
import streamlit as st
import pandas as pd

# 샘플 고객 데이터 (CSV 파일 대신 DataFrame 사용)
data = {
    "고객명": ["안수빈","조규민","김상득","김덤보","제임스"],
    "고객 정보": ["안수빈 - 20대 후반 여성, 경기도 거주(32평), 카페운영 중, 음악을 즐겨 들음",
                  "조규민 - 20대 중반 남성, 서울 거주(8평), 대학생, IT기기에 관심이 많음",
                  "김상득 - 30대 초반 남성, 서울 거주(10평), 영업직, 전자기기에 익숙하지 않음",
                  "김덤보 - 30대 초반 남성, 서울 거주(30평), 무직, 운동을 좋아함",
                  "제임스 - 30대 중반 남성, 서울 거주(25평), 개발자, 신발에 관심이 많음"
                 ],
    "보유 가전제품": ["냉장고","세탁기","TV","에어컨","스타일러"]
}
df = pd.DataFrame(data)

# 연관 제품 추천 데이터
recommendations = {
    "냉장고": "정수기, 김치냉장고",
    "세탁기": "건조기, 스타일러",
    "TV": "사운드바, 홈시어터",
    "에어컨": "공기청정기, 제습기",
    "스타일러": "건조기, 세탁기"
}

# Streamlit UI
st.set_page_config(page_title="Info and Recommend", page_icon="🧐")

# st.markdown("# 🧐 Products Recommend")
st.sidebar.header("Info and Recommend")

st.title("👨🏻‍💻 고객 정보 확인")
st.write("")
st.write("")
# 고객 정보 입력
customer_name = st.text_input("고객 이름을 입력하세요:")
st.write("")
st.write("")
# 고객 검색 및 보유 제품 조회
if customer_name:
    customer_data = df[df["고객명"] == customer_name]
    if not customer_data.empty:
        customer_info = customer_data.iloc[0]["고객 정보"]
        st.write(f"#### 🕵️‍♀️고객 정보: {customer_info}")
        owned_products = customer_data.iloc[0]["보유 가전제품"].split(", ")
        st.write(f"#### 🛒보유 제품")
        st.write(", ".join(set(owned_products)))
        st.write("")
        # 연관 제품 추천
        recommended_items = []
        for product in owned_products:
            if product in recommendations:
                recommended_items.extend(recommendations[product].split(", "))
        if recommended_items:
            st.write("#### 💡추천 제품")
            st.write(", ".join(set(recommended_items)))
        else:
            st.write("추천할 제품이 없습니다.")
    else:
        st.write("해당 고객을 찾을 수 없습니다.")
