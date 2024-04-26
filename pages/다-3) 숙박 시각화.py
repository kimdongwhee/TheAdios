import streamlit as st
import numpy as np
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium
from PIL import Image

st.set_page_config(layout='wide')
st.title('숙박업소 시각화')
st.markdown('''-----''')
df1= pd.read_excel('data/평점 4이상 숙박업소.xlsx')
@st.cache_data
def hotel_folium_gen():
    map = folium.Map(location=[35.10474134282243, 129.040661589673], zoom_start=14)
    for i in range(len(df1)):
        custom_icon = folium.CustomIcon(icon_image= 'icon/숙박업소.png', icon_size=(30, 30))
        popup_text = f"업소명: {df1['업소명'][i]}<br>평점: {df1['평점'][i]}<br>구분: {df1['구분'][i]}"
        html = folium.Html(popup_text, script=True)
        popup = folium.Popup(html, max_width=200, parse_html=False)
        try:
            folium.Marker([df1['lat'][i],df1['lng'][i]],popup=popup, icon=custom_icon).add_to(map)
        except:
            pass
    return map

st_folium(hotel_folium_gen(),use_container_width=True)