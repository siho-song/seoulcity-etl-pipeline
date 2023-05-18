import folium
import json

# 1. 지도 생성
m = folium.Map(location=[37.55465, 126.97241300000002], zoom_start=15)

# 2. JSON 데이터 로드
with open('data.json') as f:
    data = json.load(f)

# 3. 좌표 추출
coordinates = data[1]['geometry']['coordinates']

# 4. 마커 생성
marker = folium.Marker(location=coordinates)

# 5. 지도에 마커 추가
marker.add_to(m)

# 6. HTML 파일로 저장
m.save('map.html')