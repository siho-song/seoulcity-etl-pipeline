from kafka import KafkaConsumer
import time
import json
import folium
import os

consumer = KafkaConsumer(
    'seoulcity_visual',  # 수신할 토픽명
    bootstrap_servers='localhost:9092',
    auto_offset_reset='latest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

with open ("./resource/center.json" ,"r") as f:
    centerdict = json.load(f)
    

# tiles=['cartodbpositron','Stamen Toner','OpenStreetMap']
pwd = os.getcwd()
path = pwd+"/flask"

def get_newmap(AREA_NM):
    m=folium.Map(
        location=[centerdict[AREA_NM][0],centerdict[AREA_NM][1]],
        zoom_start = 17,
        tiles = 'OpenStreetMap'
    )
    return m

for message in consumer:

    
    data = message.value
    AREA_NM = data['key']
    m=get_newmap(AREA_NM)
    ROAD_TRAFFIC_STTS = data['ROAD_TRAFFIC_STTS']
    PRK_STTS=data['PRK_STTS']
    SBIKE_STTS=data['SBIKE_STTS']
    
    #도로소통정보 
    # feature_group = folium.FeatureGroup(name="")
    for road_traffic_stts in ROAD_TRAFFIC_STTS:
        road_info = road_traffic_stts["road_info"]
        polyline =folium.PolyLine(locations=road_traffic_stts["XYLIST"], 
                                  color=road_traffic_stts["COLOR"],
                                  tooltip=road_info,
                                  popup=road_info
                                  )
        polyline.add_to(m)
    m.save(path+"/templates/map/도로소통정보/"+AREA_NM+".html")
    
    
    m=get_newmap(AREA_NM)
    
    #주차장정보
    for prk_stts in PRK_STTS:
        prk_info = prk_stts["prk_info"]
        prk_color=prk_stts["COLOR"]
        prk_xylist=prk_stts["XYLIST"]
        
        marker = folium.Marker(location=prk_xylist, 
                               tooltip=prk_info, 
                               icon=folium.Icon(icon='map-marker',color=prk_color),
                               popup=prk_info
                               )
        marker.add_to(m)
    m.save(path+"/templates/map/주차장정보/"+AREA_NM+".html")
    
    
    m=get_newmap(AREA_NM)
    
    #따릉이정보
    for sbike_stts in SBIKE_STTS:
        sbike_info = sbike_stts["sbike_info"]
        sbike_color= sbike_stts["COLOR"]
        sbike_xylist=sbike_stts["XYLIST"]
        marker = folium.Marker(location=sbike_xylist, 
                               tooltip=sbike_info, 
                               icon=folium.Icon(color=sbike_color),
                               popup=sbike_info)
        marker.add_to(m)
    m.save(path+"/templates/map/따릉이정보/"+AREA_NM+".html")
    
