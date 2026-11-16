import random
import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="오늘 뭐 먹지?", page_icon="🍽️")

st.title("🍽️ 오늘의 점심 메뉴 추천")
st.write("버튼을 누르면 오늘 먹을 점심 메뉴를 랜덤으로 골라드립니다!")

# 점심 메뉴 리스트 (원하는 메뉴를 자유롭게 추가/수정하세요)
lunch_menus = [
    "김치찌개",
    "된장찌개",
    "제육볶음",
    "돈까스",
    "초밥",
    "파스타",
    "쌀국수",
    "짜장면 & 탕수육",
    "수제버거",
    "순대국밥",
    "비빔밥",
    "마라탕",
    "부대찌개",
    "냉면",
    "샌드위치",
]

# 추천 버튼
if st.button("🎲 오늘의 메뉴 뽑기", use_container_width=True):
    selected_menu = random.choice(lunch_menus)
    st.success(f"오늘의 추천 점심 메뉴는 **{selected_menu}** 입니다!")
    st.balloons()

# 전체 메뉴 후보 확인용 접이식 메뉴
with st.expander("📋 등록된 전체 메뉴 보기"):
    st.write(", ".join(lunch_menus))
