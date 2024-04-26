import streamlit as st
import numpy as np
import pandas as pd
import plotly
import plotly.graph_objects as go
from sklearn.preprocessing import MinMaxScaler
import scipy.stats as stats

st.title('년/월별 화물처리량 - 체류시간 상관분석')
st.markdown('''-----''')
ship_stayed_df=pd.read_csv('data/처리실적-체류시간_상관분석.csv').drop('Unnamed: 0',axis=1)
ship_stayed_df.rename(columns={'컨테이너':'화물처리량',
                               '체류시간_totalTime(시간)':'체류시간'},
                      inplace=True)
ship_stayed_df=ship_stayed_df.sort_values(['년도','월']).reset_index()\
    .drop('index',axis=1)
y_m=[]
for i in range(len(ship_stayed_df)):
    y_m.append(str(ship_stayed_df['년도'][i])+'-'+str(ship_stayed_df['월'][i]))
ship_stayed_df['년/월']=y_m
ship_stayed_df['년/월']=pd.to_datetime(ship_stayed_df['년/월'])
ship_stayed_df=ship_stayed_df.iloc[:,:-1]
st.dataframe(ship_stayed_df,use_container_width=True)

scaler=MinMaxScaler()
ship_stayed_scaled=pd.DataFrame(
    scaler.fit_transform(ship_stayed_df.copy()),
    columns=ship_stayed_df.columns
)
ship_stayed_scaled['년/월']=y_m

corr=stats.pearsonr(ship_stayed_scaled['화물처리량'],
                    ship_stayed_scaled['체류시간'])
st.write(f'상관계수 : {round(corr[0],3)}')
st.write(f'P-value : {round(corr[1],3)}')
st.write(f'P-value가 {round(corr[1],3)}로, 상관계수가 유의미하다고 보임')

def plotly_gen_corr():
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=ship_stayed_scaled['체류시간'],
                             y=ship_stayed_scaled['화물처리량'],
                             mode='markers',name='실측값'))

    # 추세선을 추가합니다.
    fig.add_trace(go.Scatter(
        x=ship_stayed_scaled['체류시간'],
        y=np.poly1d(np.polyfit(ship_stayed_scaled['체류시간'], ship_stayed_scaled['화물처리량'],1))\
            (ship_stayed_scaled['체류시간']),
        mode='lines',line=dict(color='red', width=2),
        name='추세선'
    ))

    fig.update_layout(title='년/월별 화물처리실적 - 체류시간(정규화)',
                    xaxis=dict(title='체류시간'),
                    yaxis=dict(title='년/월별 화물처리실적'),
                    width=600,height=600,
                    hovermode='x',
                    annotations=[
                        dict(x=-0.1,
                            y=1.1,
                            xref='paper',
                            yref='paper',
                            text=f'상관계수: {round(corr[0],3)}',
                            showarrow=False)])
    return fig
st.plotly_chart(plotly_gen_corr())

def ts_plotly_gen():
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=ship_stayed_scaled['년/월'],
                             y=ship_stayed_scaled['화물처리량'],
                             name='화물처리량',
                             line=dict(color='red')))
    fig.add_trace(go.Scatter(x=ship_stayed_scaled['년/월'],
                             y=ship_stayed_scaled['체류시간'],
                             name='체류시간',
                             line=dict(color='blue')))
    fig.update_layout(
        title='년/월별 화물처리량, 체류시간 추이',
        xaxis=dict(title='년/월'),
        hovermode='x',
        annotations=[
            dict(x=-0.03,
                y=1.15,
                xref='paper',
                yref='paper',
                text='(모든 수치는 정규화된 수치임)',
                showarrow=False)])
    return fig

st.plotly_chart(ts_plotly_gen())