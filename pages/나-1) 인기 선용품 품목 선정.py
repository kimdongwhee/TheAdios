import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import plotly
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(layout='wide')
st.title('년도 / 분기별 선용품 품목 시각화')
st.markdown('''-----''')
popular_ship_goods_18_df=pd.read_csv('data/2018년도 분기별 품목 합.csv')
popular_ship_goods_18_df['년도']=2018
popular_ship_goods_19_df=pd.read_csv('data/2019년도 분기별 품목 합.csv')
popular_ship_goods_19_df['년도']=2019
popular_ship_goods_20_df=pd.read_csv('data/2020년도 분기별 품목 합.csv')
popular_ship_goods_20_df['년도']=2020
popular_ship_goods_21_df=pd.read_csv('data/2021년도 분기별 품목 합.csv')
popular_ship_goods_21_df['년도']=2021
popular_ship_goods_22_df=pd.read_csv('data/2022년도 분기별 품목 합.csv')
popular_ship_goods_22_df['년도']=2022
popular_ship_goods_23_df=pd.read_csv('data/2023년도 분기별 품목 합.csv')
popular_ship_goods_23_df['년도']=2023

df_list=[popular_ship_goods_18_df,
         popular_ship_goods_19_df,
         popular_ship_goods_20_df,
         popular_ship_goods_21_df,
         popular_ship_goods_22_df,
         popular_ship_goods_23_df]
for i in df_list:
    i.columns=['품목','1분기','2분기','3분기','4분기','년도']
df_concated=pd.concat(df_list)

select_year=st.selectbox('년도 선택',list(set(df_concated.년도)))
df_selected=df_concated.query(f"년도=={select_year}")

title_list=[f'{select_year}년도 1분기 선용품 품목',
            f'{select_year}년도 2분기 선용품 품목',
            f'{select_year}년도 3분기 선용품 품목',
            f'{select_year}년도 4분기 선용품 품목']
def plotly_gen():
    fig=make_subplots(rows=2,cols=2,subplot_titles=title_list)
    fig.add_trace(go.Bar(x=df_selected['품목'],
                             y=df_selected['1분기'],
                             marker_color='#ffff00',
                             name='1분기'),row=1,col=1)
    fig.add_trace(go.Bar(x=df_selected['품목'],
                             y=df_selected['2분기'],
                             marker_color='#40e0d0',
                             name='2분기'),row=1,col=2)
    fig.add_trace(go.Bar(x=df_selected['품목'],
                             y=df_selected['3분기'],
                             marker_color='#ff6600',
                             name='3분기'),row=2,col=1)
    fig.add_trace(go.Bar(x=df_selected['품목'],
                             y=df_selected['4분기'],
                             marker_color='#7749f5',
                             name='4분기'),row=2,col=2)
    fig.update_layout(width=1300,height=900)
    return fig
st.plotly_chart(plotly_gen())