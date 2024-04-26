import streamlit as st
import numpy as np
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium

st.set_page_config(layout='wide')
st.title('업종별 기업 리스트 소싱')
st.markdown('''-----''')
company_list_df=pd.read_csv('data/카테고리별 기업 리스트 최종본.csv').drop('Unnamed: 0',axis=1)
company_type_list=list(set(company_list_df['카테고리']))
company_type=st.multiselect('업종 선택',
                            company_type_list)
def df_gen():
    df=company_list_df.query(f'카테고리 in {company_type}').reset_index().drop('index',axis=1)
    return df
company_selected_type=df_gen()

st.dataframe(company_selected_type,
             use_container_width=True,
             height=600)
download_df=company_selected_type.to_csv().encode('utf-8-sig')

st.download_button(
    label='다운로드',
    data=download_df,
    file_name='기업 리스트.csv',
    mime='text/csv'
)

def folium_gen():
    # 지도 생성
    map=folium.Map(location=[36.071009,127.8292126], zoom_start=6.5, tiles='CartoDB positron')
    # 마커 클러스터 생성
    marker_cluster = MarkerCluster().add_to(map)

    # 카테고리에 따라 마커 지정
    icon_paths = {
        '육류': 'icon/meat.png',
        '식품': 'icon/food.png',
        '주류': 'icon/beer.png',
        '기타': 'icon/etc.png'
    }

    # 각 업체별로 마커 생성
    for index, row in company_selected_type.iterrows():
        tooltip = f"카테고리: {row['카테고리']}<br>회사명: {row['회사명']}<br>주소: {row['주소']}<br>전화번호: {row['전화번호']}"
        icon_path = icon_paths.get(row['카테고리'], 'icon/default.png')
        icon = folium.CustomIcon(icon_path, icon_size=(40, 40))
        folium.Marker([row['lat'], row['lng']], 
                    icon=icon,
                    tooltip=tooltip).add_to(marker_cluster)
    return map

st_folium(folium_gen(),use_container_width=True)