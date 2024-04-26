import streamlit as st
import numpy as np
import pandas as pd
import plotly
import plotly.graph_objects as go
from sklearn.preprocessing import MinMaxScaler
import scipy.stats as stats

st.title('물동량 - 화물처리실적 상관분석')
st.markdown('''-----''')
scaler=MinMaxScaler()
ton_shipgoods_df=pd.read_csv('data/물동량-화물처리실적.csv').drop('Unnamed: 0',axis=1)
ton_shipgoods_df.set_index('년도',inplace=True)
ton_shipgoods_scaled=pd.DataFrame(
    scaler.fit_transform(ton_shipgoods_df),
    columns=ton_shipgoods_df.columns
)
ton_shipgoods_scaled.index=ton_shipgoods_df.index
ton_shipgoods_scaled.reset_index(inplace=True)

corr=stats.pearsonr(ton_shipgoods_scaled['물동량'],
                    ton_shipgoods_scaled['화물처리실적'])
st.dataframe(ton_shipgoods_df,use_container_width=True)
st.write(f"상관계수 : {round(corr[0],3)}")
st.write(f"P-values : {round(corr[1],3)}")
def plotly_gen_corr():
    fig=go.Figure()
    fig.add_trace(go.Scatter(
        x=ton_shipgoods_scaled['물동량'],
        y=ton_shipgoods_scaled['화물처리실적'],
        mode='markers',name='실측값'
    ))
    fig.add_trace(go.Scatter(
        x=ton_shipgoods_scaled['물동량'],
        y=np.poly1d(np.polyfit(ton_shipgoods_scaled['물동량'],ton_shipgoods_scaled['화물처리실적'],1))\
            (ton_shipgoods_scaled['물동량']),
        mode='lines',name='추세선',
        line=dict(color='red')
    ))
    fig.update_layout(title='연간 물동량 - 화물처리실적 상관분석',
                    xaxis=dict(title='물동량'),
                    yaxis=dict(title='화물처리실적'),
                    annotations=[
                        dict(x=-0.03,
                            y=1.15,
                            xref='paper',
                            yref='paper',
                            text=f'상관계수 : {round(corr[0],3)}\t(정규화된 수치로 계산)',
                            showarrow=False)])
    return fig
st.plotly_chart(plotly_gen_corr())


def plotly_gen_1():
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=ton_shipgoods_scaled['년도'],
                             y=ton_shipgoods_scaled['물동량'],
                             mode='lines',line=dict(color='blue'),
                             name='물동량'))
    fig.add_trace(go.Scatter(x=ton_shipgoods_scaled['년도'],
                             y=ton_shipgoods_scaled['화물처리실적'],
                             mode='lines',line=dict(color='red'),
                             name='화물처리실적'))
    fig.update_layout(title='연간 물동량, 화물처리실적 추이',
                    xaxis=dict(title='년도'),
                    annotations=[
                        dict(x=-0.03,
                            y=1.15,
                            xref='paper',
                            yref='paper',
                            text='(모든 수치는 정규화된 수치임)',
                            showarrow=False)])
    return fig

st.plotly_chart(plotly_gen_1())