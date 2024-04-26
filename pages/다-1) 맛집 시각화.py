import streamlit as st
import numpy as np
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium
from PIL import Image

st.set_page_config(layout='wide')
st.title('맛집 시각화')
st.markdown('''-----''')
df=pd.read_excel('data/평점 4이상 맛집리스트.xlsx',index_col=0)

@st.cache_data
def rest_folium_gen():
    map = folium.Map(location=[35.10474134282243, 129.040661589673], zoom_start=15)
    for i in range(len(df)):
        custom_icon = folium.CustomIcon(icon_image= 'icon/식당.png', icon_size=(30, 30))
        popup_text = f"가게명: {df['가게명'][i]}<br>평점: {df['평점'][i]}<br>구분: {df['구분'][i]}<br>주소 : {df['주소1'][i]}"
        html = folium.Html(popup_text, script=True)
        popup = folium.Popup(html, max_width=200, parse_html=False)
        try:
            folium.Marker([df['lat'][i],df['lng'][i]],popup= popup, icon = custom_icon).add_to(map)
        except:
            pass
    return map
st_folium(rest_folium_gen(),use_container_width=True)