import streamlit as st
import numpy as np
import pandas as pd
import osmnx as ox
import networkx as nx
from streamlit_folium import st_folium
import folium

st.markdown(
    '''
    ### 체류시간별 관광코스 시각화
    -----
    ##### 체류 7시간 관광코스(5개 코스)
    * 코스: 부산신항 - 관광지1 - 관광지2 - 맛집1 - 부산신항
    ##### 체류 3일 관광코스(4개 코스)
    * 1 day :부산신항 - 관광지1 - 맛집1 - 관광지2 - 맛집2 - 숙박
    * 2 day : 숙박 - 관광지3 - 맛집3 - 광광지4 - 맛집4 - 숙박
    * 3 day : 숙박 - 관광지5-맛집5 - 관광지 6 - 맛집 6 - 부산신항
'''
    )

# 부산신항 좌표
point=[35.078205, 128.832975]

# 7시간 추천 코스
# 1. 부산신항 - 감천문화마을 - 오륙도 스카이워크 - 생강나무 - 부산신항(2시간 33분)
@st.cache_data
def osmnx_gen7_1():
# # 지역 설정
    busan = "부산광역시, 대한민국"
    targetPoint = ox.graph_from_point(point, network_type="drive",dist=15000)
    tour1 = [35.097486,129.0105996]  #관광지1
    tour2 = [35.0993277,129.1202127]  #관광지2
    food = [35.1071441,129.0387649]  #맛집

    port_Point=ox.distance.nearest_nodes(targetPoint,point[1],point[0])  #부산항 좌표
    tour1_Point = ox.distance.nearest_nodes(targetPoint, tour1[1], tour1[0]) #관광지1 좌표
    tour2_Point = ox.distance.nearest_nodes(targetPoint, tour2[1], tour2[0]) #관광지1 좌표
    food_Point = ox.distance.nearest_nodes(targetPoint, food[1], food[0]) #맛집 좌표

    route1=nx.shortest_path(targetPoint,port_Point,tour1_Point)  #부산항 - 관광지1 최단 경로
    route2=nx.shortest_path(targetPoint,tour1_Point,tour2_Point)  #관광지1- 관광지2 최단 경로
    route3= nx.shortest_path(targetPoint,tour2_Point,food_Point) #관광지2 - 맛집 최단 경로
    route4= nx.shortest_path(targetPoint,food_Point,port_Point) #맛집- 부산항 최단경로

    # 부산항 근처 2km 운전 도로망에 루트1, 2 표시
    # 파란색이 부산항 - 맛집
    # 붉은색이 맛집 호텔
    fig,ax=ox.plot_graph_routes(targetPoint,[route1,route2,route3,route4],node_size=0.5, edge_linewidth=0.5, edge_color='white',route_colors=['red','orange','yellow','blue'])
    return fig

osmnx7_1=osmnx_gen7_1()

# 2. 부산신항 - 해동용궁사 - 오륙도 스카이워크 - 오오키니(2시간 50분)
@st.cache_data
def osmnx_gen7_2():
    targetPoint = ox.graph_from_point(point, network_type="drive",dist=15000)
    tour1 = [35.188314, 129.2232312]  #관광지1
    tour2 = [35.0993277,129.1202127]  #관광지2
    food = [35.1065653,129.037611]  #맛집

    port_Point=ox.distance.nearest_nodes(targetPoint,point[1],point[0])  #부산항 좌표
    tour1_Point = ox.distance.nearest_nodes(targetPoint, tour1[1], tour1[0]) #관광지1 좌표
    tour2_Point = ox.distance.nearest_nodes(targetPoint, tour2[1], tour2[0]) #관광지1 좌표
    food_Point = ox.distance.nearest_nodes(targetPoint, food[1], food[0]) #맛집 좌표

    route1=nx.shortest_path(targetPoint,port_Point,tour1_Point)  #부산항 - 관광지1 최단 경로
    route2=nx.shortest_path(targetPoint,tour1_Point,tour2_Point)  #관광지1- 관광지2 최단 경로
    route3= nx.shortest_path(targetPoint,tour2_Point,food_Point) #관광지2 - 맛집 최단 경로
    route4= nx.shortest_path(targetPoint,food_Point,port_Point) #맛집- 부산항 최단경로

    # 부산항 근처 2km 운전 도로망에 루트1, 2 표시
    # 파란색이 부산항 - 맛집
    # 붉은색이 맛집 호텔
    fig,ax=ox.plot_graph_routes(targetPoint,[route1,route2,route3,route4],node_size=0.5, edge_linewidth=0.5, edge_color='white',route_colors=['red','orange','yellow','blue'])
    return fig
osmnx7_2=osmnx_gen7_2()

# 3. 부산신항 - 오시리아 해안산책로 - 태종대유원지 - 할매복국(3시간 10분)
@st.cache_data
def osmnx_gen7_3():
    targetPoint = ox.graph_from_point(point, network_type="drive",dist=15000)
    tour1 = [35.1964941,129.2282823]  #관광지1
    tour2 = [35.0596604,129.0798817]  #관광지2
    food = [35.112333,129.0353778]  #맛집

    port_Point=ox.distance.nearest_nodes(targetPoint,point[1],point[0])  #부산항 좌표
    tour1_Point = ox.distance.nearest_nodes(targetPoint, tour1[1], tour1[0]) #관광지1 좌표
    tour2_Point = ox.distance.nearest_nodes(targetPoint, tour2[1], tour2[0]) #관광지1 좌표
    food_Point = ox.distance.nearest_nodes(targetPoint, food[1], food[0]) #맛집 좌표

    route1=nx.shortest_path(targetPoint,port_Point,tour1_Point)  #부산항 - 관광지1 최단 경로
    route2=nx.shortest_path(targetPoint,tour1_Point,tour2_Point)  #관광지1- 관광지2 최단 경로
    route3= nx.shortest_path(targetPoint,tour2_Point,food_Point) #관광지2 - 맛집 최단 경로
    route4= nx.shortest_path(targetPoint,food_Point,port_Point) #맛집- 부산항 최단경로

    # 부산항 근처 2km 운전 도로망에 루트1, 2 표시
    # 파란색이 부산항 - 맛집
    # 붉은색이 맛집 호텔
    fig,ax=ox.plot_graph_routes(targetPoint,[route1,route2,route3,route4],node_size=0.5, edge_linewidth=0.5, edge_color='white',route_colors=['red','orange','yellow','blue'])
    return fig
osmnx7_3=osmnx_gen7_3()

# 4. 부산신항 - 역사의 디오라마 -  감천문화마을 - 새포항물회(2시간 34분)
@st.cache_data
def osmnx_gen7_4():
    targetPoint = ox.graph_from_point(point, network_type="drive",dist=15000)
    tour1 = [35.1118743,129.0351068]  #관광지1
    tour2 = [35.097486,129.0105996]  #관광지2
    food = [35.1087054,129.03771]  #맛집

    port_Point=ox.distance.nearest_nodes(targetPoint,point[1],point[0])  #부산항 좌표
    tour1_Point = ox.distance.nearest_nodes(targetPoint, tour1[1], tour1[0]) #관광지1 좌표
    tour2_Point = ox.distance.nearest_nodes(targetPoint, tour2[1], tour2[0]) #관광지1 좌표
    food_Point = ox.distance.nearest_nodes(targetPoint, food[1], food[0]) #맛집 좌표

    route1=nx.shortest_path(targetPoint,port_Point,tour1_Point)  #부산항 - 관광지1 최단 경로
    route2=nx.shortest_path(targetPoint,tour1_Point,tour2_Point)  #관광지1- 관광지2 최단 경로
    route3= nx.shortest_path(targetPoint,tour2_Point,food_Point) #관광지2 - 맛집 최단 경로
    route4= nx.shortest_path(targetPoint,food_Point,port_Point) #맛집- 부산항 최단경로

    # 부산항 근처 2km 운전 도로망에 루트1, 2 표시
    # 파란색이 부산항 - 맛집
    # 붉은색이 맛집 호텔
    fig,ax=ox.plot_graph_routes(targetPoint,[route1,route2,route3,route4],node_size=0.5, edge_linewidth=0.5, edge_color='white',route_colors=['red','orange','yellow','blue'])
    return fig
osmnx7_4=osmnx_gen7_4()

# 5. 부산신항 - 용두산공원입구 - 역사의 디오라마- 에몽데 - 부산신항(2시간 24분)
@st.cache_data
def osmnx_gen7_5():
    targetPoint = ox.graph_from_point(point, network_type="drive",dist=15000)
    tour1 = [35.1006679,129.0324484]  #관광지1
    tour2 = [35.1118743,129.0351068]  #관광지2
    food = [35.1029819,129.0326552]  #맛집

    port_Point=ox.distance.nearest_nodes(targetPoint,point[1],point[0])  #부산항 좌표
    tour1_Point = ox.distance.nearest_nodes(targetPoint, tour1[1], tour1[0]) #관광지1 좌표
    tour2_Point = ox.distance.nearest_nodes(targetPoint, tour2[1], tour2[0]) #관광지1 좌표
    food_Point = ox.distance.nearest_nodes(targetPoint, food[1], food[0]) #맛집 좌표

    route1=nx.shortest_path(targetPoint,port_Point,tour1_Point)  #부산항 - 관광지1 최단 경로
    route2=nx.shortest_path(targetPoint,tour1_Point,tour2_Point)  #관광지1- 관광지2 최단 경로
    route3= nx.shortest_path(targetPoint,tour2_Point,food_Point) #관광지2 - 맛집 최단 경로
    route4= nx.shortest_path(targetPoint,food_Point,port_Point) #맛집- 부산항 최단경로

    # 부산항 근처 2km 운전 도로망에 루트1, 2 표시
    # 파란색이 부산항 - 맛집
    # 붉은색이 맛집 호텔
    fig,ax=ox.plot_graph_routes(targetPoint,[route1,route2,route3,route4],node_size=0.5, edge_linewidth=0.5, edge_color='white',route_colors=['red','orange','yellow','blue'])
    return fig
osmnx7_5=osmnx_gen7_5()

# 3일 추천코스

@st.cache_data
def osmnx_gen_3d_1():
    targetPoint = ox.graph_from_point(point, network_type="drive",dist=15000)
    tour1 = [35.1006679,129.0324484]  #관광지1 -감천문화마을
    tour2 = [35.188314, 129.2232312]  #관광지2 -해동용궁사
    tour3 = [35.1666396,129.0552696]  #관광지3 -부산시민공원
    tour4 = [35.1163438697633,128.90591723952588]
    #tour4 = [35.1057734,129.1186902]  #관광지4 -이기대 농바위
    tour5 = [35.1006679,129.0324484]  #관광지5- 용두산공원
    tour6 = [35.1964941,129.2282823]  #관광지6- 오시리아 해안산책로

    food1 = [35.1078578,129.0373338]  #맛집1 - 진미식당
    food2 = [35.1118743,129.0351068]  #맛집2- 종필이집
    food3 = [35.1090718,129.0381316]  #맛집3- 대하가야밀면
    food4 = [35.1046749,129.0356986]  #맛집4- 시민카츠
    food5 = [35.1071441,129.0387649]  #맛집5- 생강나무
    food6 = [35.1079918,129.0376519]  #맛집6- 유원

    hotel1= [35.1159158,129.0388327]  #호텔1-디노호텔

    port_Point=ox.distance.nearest_nodes(targetPoint,point[1],point[0])  #부산항 좌표

    tour1_Point = ox.distance.nearest_nodes(targetPoint, tour1[1], tour1[0]) #관광지1 좌표
    tour2_Point = ox.distance.nearest_nodes(targetPoint, tour2[1], tour2[0]) #관광지2 좌표
    tour3_Point = ox.distance.nearest_nodes(targetPoint, tour3[1], tour3[0]) #관광지3 좌표
    tour4_Point = ox.distance.nearest_nodes(targetPoint, tour4[1], tour4[0]) #관광지4 좌표
    tour5_Point = ox.distance.nearest_nodes(targetPoint, tour5[1], tour5[0]) #관광지5 좌표
    tour6_Point = ox.distance.nearest_nodes(targetPoint, tour6[1], tour6[0]) #관광지6 좌표

    food1_Point = ox.distance.nearest_nodes(targetPoint, food1[1], food1[0]) #맛집1 좌표
    food2_Point = ox.distance.nearest_nodes(targetPoint, food2[1], food2[0]) #맛집2 좌표
    food3_Point = ox.distance.nearest_nodes(targetPoint, food3[1], food3[0]) #맛집3 좌표
    food4_Point = ox.distance.nearest_nodes(targetPoint, food4[1], food4[0]) #맛집4 좌표
    food5_Point = ox.distance.nearest_nodes(targetPoint, food5[1], food5[0]) #맛집5 좌표
    food6_Point = ox.distance.nearest_nodes(targetPoint, food6[1], food6[0]) #맛집6 좌표

    hotel_Point = ox.distance.nearest_nodes(targetPoint, hotel1[1], hotel1[0]) #호텔1 좌표

    #1일차
    route1=nx.shortest_path(targetPoint,port_Point,tour1_Point)  #부산항 - 관광지1 최단 경로
    route2=nx.shortest_path(targetPoint,tour1_Point,food1_Point)  #관광지1- 맛집1 최단 경로
    route3= nx.shortest_path(targetPoint,food1_Point,tour2_Point) #맛집1 - 관광지2 최단 경로
    route4= nx.shortest_path(targetPoint,tour2_Point,food2_Point) #관광지2-맛집2 최단경로
    route5= nx.shortest_path(targetPoint,food2_Point,hotel_Point) #맛집2-숙박 최단경로

    #2일차
    route6= nx.shortest_path(targetPoint,hotel_Point,tour3_Point) #숙박-관광지3 최단경로
    route7= nx.shortest_path(targetPoint,tour3_Point,food3_Point) #관광지3-맛집3 최단경로
    route8= nx.shortest_path(targetPoint,food3_Point,tour4_Point) #맛집3-관광지4 최단경로
    route9= nx.shortest_path(targetPoint,tour4_Point,food4_Point) #관광지4-맛집4 최단경로
    route10= nx.shortest_path(targetPoint,food4_Point,hotel_Point) #맛집4-숙박 최단경로

    #3일차
    route11= nx.shortest_path(targetPoint,hotel_Point,tour5_Point) #숙박-관광지5 최단경로
    route12= nx.shortest_path(targetPoint,tour5_Point,food5_Point) #관광지5-맛집5 최단경로
    route13= nx.shortest_path(targetPoint,food5_Point,tour6_Point) #맛집5-관광지6 최단경로
    route14= nx.shortest_path(targetPoint,tour6_Point,food6_Point) #관광지6-맛집6 최단경로
    route15= nx.shortest_path(targetPoint,food6_Point,port_Point) #맛집6-부산신항 최단경로

    # 부산항 근처 2km 운전 도로망에 루트1, 2 표시
    # 파란색이 부산항 - 맛집
    # 붉은색이 맛집 호텔
    fig,ax=ox.plot_graph_routes(targetPoint,[route1,route2,route3,route4,route5,route6,route7
                                    ,route8,route9,route10,route11,route12,route13,route14,route15]
                        ,node_size=0.2, edge_linewidth=0.5, edge_color='white',
                        route_colors=['red','orange','yellow','green','blue','red','orange','yellow','green','blue',
                                    'red','orange','yellow','green','blue'])
    return fig
osmnx_3d_1=osmnx_gen_3d_1()


@st.cache_data
def osmnx_gen_3d_2():
    targetPoint = ox.graph_from_point(point, network_type="drive",dist=15000)
    tour2 = [35.1006679,129.0324484]  #관광지1 -감천문화마을
    tour1 = [35.188314, 129.2232312]  #관광지2 -해동용궁사
    tour4 = [35.1666396,129.0552696]  #관광지3 -부산시민공원
    tour3 = [35.1057734,129.1186902]  #관광지4 -이기대 농바위
    tour6 = [35.1006679,129.0324484]  #관광지5- 용두산공원
    tour5 = [35.1964941,129.2282823]  #관광지6- 오시리아 해안산책로

    food6 = [35.1078578,129.0373338]  #맛집1 - 진미식당
    food5 = [35.1118743,129.0351068]  #맛집2- 종필이집
    food4 = [35.1090718,129.0381316]  #맛집3- 대하가야밀면
    food3 = [35.1046749,129.0356986]  #맛집4- 시민카츠
    food2 = [35.1071441,129.0387649]  #맛집5- 생강나무
    food1 = [35.1079918,129.0376519]  #맛집6- 유원

    hotel1= [35.1159158,129.0388327]  #호텔1-디노호텔

    port_Point=ox.distance.nearest_nodes(targetPoint,point[1],point[0])  #부산항 좌표

    tour1_Point = ox.distance.nearest_nodes(targetPoint, tour1[1], tour1[0]) #관광지1 좌표
    tour2_Point = ox.distance.nearest_nodes(targetPoint, tour2[1], tour2[0]) #관광지2 좌표
    tour3_Point = ox.distance.nearest_nodes(targetPoint, tour3[1], tour3[0]) #관광지3 좌표
    tour4_Point = ox.distance.nearest_nodes(targetPoint, tour4[1], tour4[0]) #관광지4 좌표
    tour5_Point = ox.distance.nearest_nodes(targetPoint, tour5[1], tour5[0]) #관광지5 좌표
    tour6_Point = ox.distance.nearest_nodes(targetPoint, tour6[1], tour6[0]) #관광지6 좌표

    food1_Point = ox.distance.nearest_nodes(targetPoint, food1[1], food1[0]) #맛집1 좌표
    food2_Point = ox.distance.nearest_nodes(targetPoint, food2[1], food2[0]) #맛집2 좌표
    food3_Point = ox.distance.nearest_nodes(targetPoint, food3[1], food3[0]) #맛집3 좌표
    food4_Point = ox.distance.nearest_nodes(targetPoint, food4[1], food4[0]) #맛집4 좌표
    food5_Point = ox.distance.nearest_nodes(targetPoint, food5[1], food5[0]) #맛집5 좌표
    food6_Point = ox.distance.nearest_nodes(targetPoint, food6[1], food6[0]) #맛집6 좌표

    hotel_Point = ox.distance.nearest_nodes(targetPoint, hotel1[1], hotel1[0]) #호텔1 좌표

    #1일차
    route1=nx.shortest_path(targetPoint,port_Point,tour1_Point)  #부산항 - 관광지1 최단 경로
    route2=nx.shortest_path(targetPoint,tour1_Point,food1_Point)  #관광지1- 맛집1 최단 경로
    route3= nx.shortest_path(targetPoint,food1_Point,tour2_Point) #맛집1 - 관광지2 최단 경로
    route4= nx.shortest_path(targetPoint,tour2_Point,food2_Point) #관광지2-맛집2 최단경로
    route5= nx.shortest_path(targetPoint,food2_Point,hotel_Point) #맛집2-숙박 최단경로

    #2일차
    route6= nx.shortest_path(targetPoint,hotel_Point,tour3_Point) #숙박-관광지3 최단경로
    route7= nx.shortest_path(targetPoint,tour3_Point,food3_Point) #관광지3-맛집3 최단경로
    route8= nx.shortest_path(targetPoint,food3_Point,tour4_Point) #맛집3-관광지4 최단경로
    route9= nx.shortest_path(targetPoint,tour4_Point,food4_Point) #관광지4-맛집4 최단경로
    route10= nx.shortest_path(targetPoint,food4_Point,hotel_Point) #맛집4-숙박 최단경로

    #3일차
    route11= nx.shortest_path(targetPoint,hotel_Point,tour5_Point) #숙박-관광지5 최단경로
    route12= nx.shortest_path(targetPoint,tour5_Point,food5_Point) #관광지5-맛집5 최단경로
    route13= nx.shortest_path(targetPoint,food5_Point,tour6_Point) #맛집5-관광지6 최단경로
    route14= nx.shortest_path(targetPoint,tour6_Point,food6_Point) #관광지6-맛집6 최단경로
    route15= nx.shortest_path(targetPoint,food6_Point,port_Point) #맛집6-부산신항 최단경로

    # 부산항 근처 2km 운전 도로망에 루트1, 2 표시
    # 파란색이 부산항 - 맛집
    # 붉은색이 맛집 호텔
    fig,ax=ox.plot_graph_routes(targetPoint,[route1,route2,route3,route4,route5,route6,route7,route8,route9,route10,route11,route12,route13,route14,route15]
                        ,node_size=0.2, edge_linewidth=0.5, edge_color='white',
                        route_colors=['red','orange','yellow','green','blue','red','orange','yellow','green','blue',
                                    'red','orange','yellow','green','blue'])
    return fig
osmnx_3d_2=osmnx_gen_3d_2()


@st.cache_data
def osmnx_gen_3d_3():
    targetPoint = ox.graph_from_point(point, network_type="drive",dist=15000)
    tour1 = [35.0993277,129.1202127]  #관광지1 -오륙도 스카이워크
    tour2 = [35.188314, 129.2232312]  #관광지2 -해동용궁사
    tour3 = [35.1006679,129.0324484]  #관광지3 -다이아몬드 타워
    tour4 = [35.1057734,129.1186902]  #관광지4 -이기대 농바위
    tour5 = [35.0596604,129.0798817]  #관광지5- 태종대유원지
    tour6 = [35.1118743,129.0351068]  #관광지6- 역사의 디오라마

    food1 = [35.1079788,129.0373868]  #맛집1 - 대영정
    food2 = [35.1044444,129.0357154]  #맛집2- 말자씨부엌
    food3 = [35.1090718,129.0381316]  #맛집3- 대하가야밀면
    food4 = [35.1042934,129.0353455]  #맛집4- 상짱
    food5 = [35.1071441,129.0387649]  #맛집5- 생강나무
    food6 = [35.1043393,129.0357391]  #맛집6- 홍문

    hotel1= [35.1012701,129.0248275]  #호텔1-지엔비호텔

    port_Point=ox.distance.nearest_nodes(targetPoint,point[1],point[0])  #부산항 좌표

    tour1_Point = ox.distance.nearest_nodes(targetPoint, tour1[1], tour1[0]) #관광지1 좌표
    tour2_Point = ox.distance.nearest_nodes(targetPoint, tour2[1], tour2[0]) #관광지2 좌표
    tour3_Point = ox.distance.nearest_nodes(targetPoint, tour2[1], tour2[0]) #관광지3 좌표
    tour4_Point = ox.distance.nearest_nodes(targetPoint, tour2[1], tour2[0]) #관광지4 좌표
    tour5_Point = ox.distance.nearest_nodes(targetPoint, tour2[1], tour2[0]) #관광지5 좌표
    tour6_Point = ox.distance.nearest_nodes(targetPoint, tour2[1], tour2[0]) #관광지6 좌표

    food1_Point = ox.distance.nearest_nodes(targetPoint, food1[1], food1[0]) #맛집1 좌표
    food2_Point = ox.distance.nearest_nodes(targetPoint, food2[1], food2[0]) #맛집2 좌표
    food3_Point = ox.distance.nearest_nodes(targetPoint, food3[1], food3[0]) #맛집3 좌표
    food4_Point = ox.distance.nearest_nodes(targetPoint, food4[1], food4[0]) #맛집4 좌표
    food5_Point = ox.distance.nearest_nodes(targetPoint, food5[1], food5[0]) #맛집5 좌표
    food6_Point = ox.distance.nearest_nodes(targetPoint, food6[1], food6[0]) #맛집6 좌표

    hotel_Point = ox.distance.nearest_nodes(targetPoint, hotel1[1], hotel1[0]) #호텔1 좌표

    #1일차
    route1=nx.shortest_path(targetPoint,port_Point,tour1_Point)  #부산항 - 관광지1 최단 경로
    route2=nx.shortest_path(targetPoint,tour1_Point,food1_Point)  #관광지1- 맛집1 최단 경로
    route3= nx.shortest_path(targetPoint,food1_Point,tour2_Point) #맛집1 - 관광지2 최단 경로
    route4= nx.shortest_path(targetPoint,tour2_Point,food2_Point) #관광지2-맛집2 최단경로
    route5= nx.shortest_path(targetPoint,food2_Point,hotel_Point) #맛집2-숙박 최단경로

    #2일차
    route6= nx.shortest_path(targetPoint,hotel_Point,tour3_Point) #숙박-관광지3 최단경로
    route7= nx.shortest_path(targetPoint,tour3_Point,food3_Point) #관광지3-맛집3 최단경로
    route8= nx.shortest_path(targetPoint,food3_Point,tour4_Point) #맛집3-관광지4 최단경로
    route9= nx.shortest_path(targetPoint,tour4_Point,food4_Point) #관광지4-맛집4 최단경로
    route10= nx.shortest_path(targetPoint,food4_Point,hotel_Point) #맛집4-숙박 최단경로

    #3일차
    route11= nx.shortest_path(targetPoint,hotel_Point,tour5_Point) #숙박-관광지5 최단경로
    route12= nx.shortest_path(targetPoint,tour5_Point,food5_Point) #관광지5-맛집5 최단경로
    route13= nx.shortest_path(targetPoint,food5_Point,tour6_Point) #맛집5-관광지6 최단경로
    route14= nx.shortest_path(targetPoint,tour6_Point,food6_Point) #관광지6-맛집6 최단경로
    route15= nx.shortest_path(targetPoint,food6_Point,port_Point) #맛집6-부산신항 최단경로

    # 부산항 근처 2km 운전 도로망에 루트1, 2 표시
    # 파란색이 부산항 - 맛집
    # 붉은색이 맛집 호텔
    fig,ax=ox.plot_graph_routes(targetPoint,[route1,route2,route3,route4,route5,route6,route7
                                    ,route8,route9,route10,route11,route12,route13,route14,route15]
                        ,node_size=0.2, edge_linewidth=0.5, edge_color='white',
                        route_colors=['red','orange','yellow','green','blue','red','orange','yellow','green','blue',
                                    'red','orange','yellow','green','blue'])
    return fig
osmnx_3d_3=osmnx_gen_3d_3()


@st.cache_data
def osmnx_gen_3d_4():
    targetPoint = ox.graph_from_point(point, network_type="drive",dist=15000)
    tour5 = [35.0993277,129.1202127]  #관광지1 -오륙도 스카이워크
    tour2 = [35.188314, 129.2232312]  #관광지2 -해동용궁사
    tour3 = [35.1006679,129.0324484]  #관광지3 -다이아몬드 타워
    tour4 = [35.1057734,129.1186902]  #관광지4 -이기대 농바위
    tour6 = [35.0596604,129.0798817]  #관광지5- 태종대유원지
    tour1 = [35.1118743,129.0351068]  #관광지6- 역사의 디오라마

    food5 = [35.1079788,129.0373868]  #맛집1 - 대영정
    food6 = [35.1044444,129.0357154]  #맛집2- 말자씨부엌
    food2 = [35.1090718,129.0381316]  #맛집3- 대하가야밀면
    food3 = [35.2052664,129.0847143]  #맛집4- 상짱
    food4 = [35.1071441,129.0387649]  #맛집5- 생강나무
    food1 = [35.1043393,129.0357391]  #맛집6- 홍문

    hotel1= [35.1012701,129.0248275]  #호텔1-지엔비호텔

    port_Point=ox.distance.nearest_nodes(targetPoint,point[1],point[0])  #부산항 좌표

    tour1_Point = ox.distance.nearest_nodes(targetPoint, tour1[1], tour1[0]) #관광지1 좌표
    tour2_Point = ox.distance.nearest_nodes(targetPoint, tour2[1], tour2[0]) #관광지2 좌표
    tour3_Point = ox.distance.nearest_nodes(targetPoint, tour3[1], tour3[0]) #관광지3 좌표
    tour4_Point = ox.distance.nearest_nodes(targetPoint, tour4[1], tour4[0]) #관광지4 좌표
    tour5_Point = ox.distance.nearest_nodes(targetPoint, tour5[1], tour5[0]) #관광지5 좌표
    tour6_Point = ox.distance.nearest_nodes(targetPoint, tour6[1], tour6[0]) #관광지6 좌표

    food1_Point = ox.distance.nearest_nodes(targetPoint, food1[1], food1[0]) #맛집1 좌표
    food2_Point = ox.distance.nearest_nodes(targetPoint, food2[1], food2[0]) #맛집2 좌표
    food3_Point = ox.distance.nearest_nodes(targetPoint, food3[1], food3[0]) #맛집3 좌표
    food4_Point = ox.distance.nearest_nodes(targetPoint, food4[1], food4[0]) #맛집4 좌표
    food5_Point = ox.distance.nearest_nodes(targetPoint, food5[1], food5[0]) #맛집5 좌표
    food6_Point = ox.distance.nearest_nodes(targetPoint, food6[1], food6[0]) #맛집6 좌표

    hotel_Point = ox.distance.nearest_nodes(targetPoint, hotel1[1], hotel1[0]) #호텔1 좌표

    #1일차
    route1=nx.shortest_path(targetPoint,port_Point,tour1_Point)  #부산항 - 관광지1 최단 경로
    route2=nx.shortest_path(targetPoint,tour1_Point,food1_Point)  #관광지1- 맛집1 최단 경로
    route3= nx.shortest_path(targetPoint,food1_Point,tour2_Point) #맛집1 - 관광지2 최단 경로
    route4= nx.shortest_path(targetPoint,tour2_Point,food2_Point) #관광지2-맛집2 최단경로
    route5= nx.shortest_path(targetPoint,food2_Point,hotel_Point) #맛집2-숙박 최단경로

    #2일차
    route6= nx.shortest_path(targetPoint,hotel_Point,tour3_Point) #숙박-관광지3 최단경로
    route7= nx.shortest_path(targetPoint,tour3_Point,food3_Point) #관광지3-맛집3 최단경로
    route8= nx.shortest_path(targetPoint,food3_Point,tour4_Point) #맛집3-관광지4 최단경로
    route9= nx.shortest_path(targetPoint,tour4_Point,food4_Point) #관광지4-맛집4 최단경로
    route10= nx.shortest_path(targetPoint,food4_Point,hotel_Point) #맛집4-숙박 최단경로

    #3일차
    route11= nx.shortest_path(targetPoint,hotel_Point,tour5_Point) #숙박-관광지5 최단경로
    route12= nx.shortest_path(targetPoint,tour5_Point,food5_Point) #관광지5-맛집5 최단경로
    route13= nx.shortest_path(targetPoint,food5_Point,tour6_Point) #맛집5-관광지6 최단경로
    route14= nx.shortest_path(targetPoint,tour6_Point,food6_Point) #관광지6-맛집6 최단경로
    route15= nx.shortest_path(targetPoint,food6_Point,port_Point) #맛집6-부산신항 최단경로

    # 부산항 근처 2km 운전 도로망에 루트1, 2 표시
    # 파란색이 부산항 - 맛집
    # 붉은색이 맛집 호텔
    fig,ax=ox.plot_graph_routes(targetPoint,[route1,route2,route3,route4,route5,route6,route7
                                    ,route8,route9,route10,route11,route12,route13,route14,route15]
                        ,node_size=0.2, edge_linewidth=0.5, edge_color='white',
                        route_colors=['red','orange','yellow','green','blue','red','orange','yellow','green','blue',
                                    'red','orange','yellow','green','blue'])
    return fig
osmnx_3d_4=osmnx_gen_3d_4()

osmnx_fig=[osmnx7_1,osmnx7_2,osmnx7_3,osmnx7_4,osmnx7_5,
           osmnx_3d_1,osmnx_3d_2,osmnx_3d_3,osmnx_3d_4]
courses=['부산신항 - 감천문화마을 - 오륙도 스카이워크 - 생강나무 - 부산신항',
         '부산신항 - 해동용궁사 - 오륙도 스카이워크 - 오오키니-부산신항',
         '부산신항 - 오시리아 해안산책로 - 태종대유원지 - 할매복국 -부산신항',
         '부산신항 - 역사의 디오라마 -  감천문화마을 - 새포항물회 - 부산신항',
         '부산신항 - 용두산공원입구 - 역사의 디오라마- 에몽데 - 부산신항',
         ['* 1day: 부산신항 - 감천문화마을 - 진미식당 - 해동용궁사 - 종필이집 - 디노호텔  \
          * 2day: 디노호텔 - 부산시민공원 - 대하가야밀면 - 이기대 농바위 - 시민카츠 - 디노호텔  \
          * 3day: 디노호텔 - 용두산공원 - 생강나무 - 오시리아 해안산책로 - 유원 - 부산신항'][0],
          ['* 1day: 부산신항 - 해동용궁사 - 유원 - 감천문화마을 - 생강나무 - 디노호텔  \
           * 2day: 디노호텔 - 이기대 농바위 - 시민카츠 - 부산시민공원 - 대하가야 밀면 - 디노호텔  \
           * 3day: 디노호텔 - 오시리아 해안산책로 - 종필이집 - 용두산공원 - 진미식당 - 부산신항'][0],
           ['* 1day: 부산신항 - 오륙도 스카이워크 - 대영정 - 해동용궁사 - 말자씨부엌 - 지엔비호텔  \
            * 2day: 지엔비호텔 - 다이아몬드 타워 - 대하가야밀면 - 이기대 농바위 - 상짱 - 지엔비호텔  \
            * 3day: 지엔비호텔 - 태종대 유원지 - 생강나무 - 역사의 디오라마 - 홍문 - 부산신항'][0],
            ['* 1day: 부산신항 - 역사의 디오라마 - 홍문 - 해동용궁사 - 대하가야밀면 - 지엔비호텔  \
             * 2day: 지엔비호텔 - 다이아몬드 타워 - 상짱 -  - 상짱 - 이기대 농바위- 지엔비호텔  \
             * 3day: 지엔비호텔 - 오륙도 스카이워크 - 대영정 - 태종대유원지 - 말자씨부엌 - 부산신항'][0]]
course_df=pd.DataFrame({
    '체류시간':['7시간','7시간','7시간','7시간','7시간',
             '3일','3일','3일','3일'],
    '코스':courses,
    'Fig':osmnx_fig
})
time_select=st.selectbox('체류 시간 선택',list(set(course_df['체류시간'])))
course_df_time_select=course_df.query(f"체류시간=='{time_select}'")
course_select=st.selectbox('코스 선택',course_df_time_select['코스'])
course_final=course_df_time_select.query(f"코스=='{course_select}'")\
    .reset_index().drop('index',axis=1)

st.pyplot(course_final['Fig'][0],use_container_width=True)