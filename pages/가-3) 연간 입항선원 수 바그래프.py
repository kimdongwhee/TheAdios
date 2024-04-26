import streamlit as st
import numpy as np
import pandas as pd
import plotly
import plotly.graph_objects as go

st.title('연간 입항 외국인 선원 추이')
st.markdown('''
-----------
''')
busan_sailors_df=pd.read_excel('data/항구별 출입항 선원수.xlsx',
                               header=[0,1,2],index_col=0)
year_list=list(range(2009,2022))
col_list=[]
for i in year_list:
    col=busan_sailors_df[str(i)][('입항','선원수 (명)')][1]
    col_list.append(col)

busan_sailor_num_df=pd.DataFrame(col_list,columns=['입항 선원수(명)'],index=year_list)
busan_sailor_num_df=busan_sailor_num_df.reset_index().rename(columns={'index':'년도'})

def ts_plotly_bar_gen():
    fig=go.Figure()
    fig.add_trace(go.Bar(x=busan_sailor_num_df['년도'],y=busan_sailor_num_df['입항 선원수(명)'],
                        text=busan_sailor_num_df['입항 선원수(명)'],textposition='outside'))
    fig.update_layout(title='연간 외국인 선원 수 ',
                      hovermode='x',
                    xaxis=dict(title='년도'),
                    yaxis=dict(title='연간 외국인 선원 수(단위:명)'))
    return fig
st.markdown('''
            ##### 20년도 급감 -> 코로나 이슈로 유추할 수 있음
            ##### 21년도 이후 자료가 없는 점이 아쉬움
''')
st.plotly_chart(ts_plotly_bar_gen())