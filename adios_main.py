import streamlit as st
import pandas as pd

st.header("The Team Adios Portfolio :people_holding_hands:")

st.subheader(":one: Team member and Role")
team_member = pd.DataFrame({
    "팀원": ["김동휘", "김성일", "임경란", "정현수", "서한울", "신대근"],
    "R&R(Role and Responsibility)" : ["기획, DB모델링, Back-End, LangChain", "데이터 수집/가공, 모델구현/검증", "LangChain, 모델구현/검증", "데이터 수집/가공, 모델구현/검증", "데이터 수집/가공, 모델구현/검증", "데이터 수집/가공, 모델구현/검증"]

})
st.dataframe(team_member, hide_index=True, use_container_width=True)
st.subheader(":two: Team Project")

st.markdown("(1) 선용폼 구매 플랫폼 구축을 위한 타당성 분석 및 외국인 선원 체류시간별 코스/맛집 추천")
st.video("./useData/Busan/busan_video.mp4")

st.markdown("(2) 해외 축구팬들을 위한 OOF(Oracle Of Football) 플랫폼")
st.video("./useData/OOF/OOF_Video.mp4")