import streamlit as st
import numpy as np
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium
from PIL import Image

st.set_page_config(layout='wide')
st.title('관광지 시각화')
st.markdown('''-----''')
df2=pd.read_excel('data/관광지 위경도.xlsx')
@st.cache_data
def place_folium_gen():
    map = folium.Map(location=[35.10474134282243, 129.040661589673], zoom_start=11)
    for i in range(len(df2)):
        custom_icon = folium.CustomIcon(icon_image= 'icon/관광지.png', icon_size=(30, 30))
        popup_text = f"관광지명: {df2['title'][i]}<br>평점: {df2['rating'][i]}<br>구분: {df2['category'][i]}<br>주소: {df2['address'][i]}"
        html = folium.Html(popup_text, script=True)
        popup = folium.Popup(html, max_width=200, parse_html=False)
        try:
            folium.Marker([df2['lat'][i],df2['lng'][i]],popup=popup, icon=custom_icon).add_to(map)
        except:
            pass
    return map
st_folium(place_folium_gen(),use_container_width=True)