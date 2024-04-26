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
