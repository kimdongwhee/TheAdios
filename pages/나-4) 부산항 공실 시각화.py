import streamlit as st
import numpy as np
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium

st.title('부산항 근처 공실 시각화')
st.markdown('''-----''')

real_estate_df=pd.read_csv('data/부산항 창고_6개 구역 전체 파일.csv', index_col=0)

# 매매가  단위변환(1) : 억으로 끝나는 값
def convert_to_manwon(s):
    if s == '-':
        return None    

    s = s.replace('억', '').replace(',', '')
    # 숫자로 변환
    try:
        num = int(s)
    except ValueError:
        return None    
    # 만원 단위로 변환하여 반환
    return num * 10000

# 매매가 열의 값을 만원 단위로 변환하여 새로운 열에 저장
real_estate_df['매매가_1'] = real_estate_df['매매가'].apply(convert_to_manwon)

# 억 단위변환(2) : 값이 억으로 끝나는 경우가 아닐 경우
def convert_to_manwon(s):
    if s == '-':
        return None    

# '억'을 기준으로 문자열을 분할
    unit_index = s.find('억')
    if unit_index != -1:
        billion_part = s[:unit_index]
        after_billion_part = s[unit_index+1:].replace(',', '')
    else:
        return None
    
    # '억' 앞의 숫자와 '억' 뒤의 숫자를 정수로 변환
    try:
        billion = int(billion_part)
        after_billion = int(after_billion_part)
    except ValueError:
        return None
    
    # 만원 단위로 변환하여 반환
    return billion * 10000 + after_billion

real_estate_df['매매가_2'] = real_estate_df['매매가'].apply(convert_to_manwon)

# 두 칼럼 합치기

# NaN 값을 0원으로 변경
real_estate_df['매매가_1'] = real_estate_df['매매가_1'].fillna(0)
real_estate_df['매매가_2'] = real_estate_df['매매가_2'].fillna(0)

real_estate_df['매매가(단위:만원)'] = real_estate_df['매매가_1'] + real_estate_df['매매가_2']

# 필요한 칼럼만 불러오기
group = real_estate_df[['구분', '타입', '계약면적(㎡)', '전용면적(㎡)', '대지면적(㎡)','매매가(단위:만원)', '보증금 (단위: 만원)','월세(단위:만원)']]
group.replace('-', 0, inplace=True)
# 데이터타입 변경
group[['계약면적(㎡)', '전용면적(㎡)', '대지면적(㎡)', 
       '매매가(단위:만원)', '보증금 (단위: 만원)', '월세(단위:만원)']] = group[['계약면적(㎡)', '전용면적(㎡)', '대지면적(㎡)', 
                                                            '매매가(단위:만원)', '보증금 (단위: 만원)', '월세(단위:만원)']].astype(float).round().astype(int)
# 타입별 개수 추가
group_type = group.groupby(['구분','타입']).size().reset_index(name='타입별 개수')
# groupby로 계산
array_grouped = group.groupby(['구분', '타입']).agg({'계약면적(㎡)': 'mean', '전용면적(㎡)': 'mean', '대지면적(㎡)': 'mean',
                                                   '매매가(단위:만원)' : 'mean', '보증금 (단위: 만원)' :'mean', '월세(단위:만원)':'mean'}).reset_index()
# array_grouped에 group_type 합치기
merge_grouped = pd.merge(group_type, array_grouped, on=['구분','타입'], how='inner')
# 다시 반올림 및 데이터 타입 정수로 변경
merge_grouped[['계약면적(㎡)', '전용면적(㎡)', '대지면적(㎡)', 
       '매매가(단위:만원)', '보증금 (단위: 만원)', '월세(단위:만원)']] = merge_grouped[['계약면적(㎡)', '전용면적(㎡)', '대지면적(㎡)', 
                                                            '매매가(단위:만원)', '보증금 (단위: 만원)', '월세(단위:만원)']].astype(float).round().astype(int)

def folium_gen():
    map = folium.Map(location=[35.0673692,128.8521182], zoom_start=12.2)
    # 각 지역별 반지름 지정
    #radius_dict = {'명지동': 70, '성북동': 35, '송정동': 50, '신호동': 55, '용원동': 35,'천성동': 40}
    radius_dict = {'명지동': 70, '성북동': 30, '송정동': 50, '신호동': 60, '용원동': 40,'천성동': 35}

    # 각 지역별 위도, 경도 지정
    location_dict = {'명지동': [35.1079767,128.924848], '성북동': [35.060441,128.8173813], '송정동': [35.0978089,128.8487525],
                    '신호동': [35.0904701,128.884458], '용원동': [35.0957021,128.8183684], '천성동': [35.0353557,128.8200421]}
    for i in merge_grouped['구분'].unique():
        df_subset = merge_grouped[merge_grouped['구분'] == i]
        tooltip = f"지역 : {i}<br>"
        
        for j, row in df_subset.iterrows():
            if row['타입'] == '매매':
                tooltip += f"1. 매매 : {row['타입별 개수']}곳<br>"
                tooltip += f"- 평균 평수 : 계약면적 {row['계약면적(㎡)']:,}㎡ / 전용면적 {row['전용면적(㎡)']:,}㎡ / 대지면적 {row['대지면적(㎡)']:,}㎡<br>"
                tooltip += f"- 평균 매매가: {int(row['매매가(단위:만원)']):,}만원<br>"
            elif row['타입'] == '월세':
                tooltip += f"2. 월세 : {row['타입별 개수']}곳<br>"
                tooltip += f"- 평균 평수 : 계약면적 {row['계약면적(㎡)']:,}㎡ / 전용면적 {row['전용면적(㎡)']:,}㎡ / 대지면적 {row['대지면적(㎡)']:,}㎡<br>"
                tooltip += f"- 평균 보증금: {int(row['보증금 (단위: 만원)']):,}만원<br>"
                tooltip += f"- 평균 월세: {int(row['월세(단위:만원)']):,}만원<br>"
                
        location = location_dict.get(i)
        radius = radius_dict.get(i, 80)
        folium.CircleMarker(location=location, radius=radius, fill=True, color = '#f53b3b', 
                            fill_color = 'yellow', fill_opacity = '25%', tooltip=tooltip)\
                                .add_to(map)
        
    folium.Marker(location=[35.0809179, 128.8349832], tooltip='부산신항만', 
                  icon=folium.Icon(color='red', icon='ship', prefix='fa'), 
                  min_width=500, max_width=500).add_to(map)
    return map

st_folium(folium_gen(),use_container_width=True)