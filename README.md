
# seoulcity-Realtime-etl-pipeline 
### 서울 열린데이터 광장 open api 를 활용한 etl pipeline 구축 및 시각화 프로젝트
---

## Version
OS : ubuntu:22.04 <br>
JDK : java-8-openjdk-amd64 <br>
Python : python3.10 <br>
Kafka : kafka_2.13-2.7.2 <br>
Spark : spark_3.4.0 <br>
Mongodb : mongo_6.0.4 <br>

---
## Architecture
<img width="945" alt="화면 캡처 2023-06-07 142602" src="https://github.com/siho-song/seoulcity-etl-pipeline/assets/79968994/2d152193-eae0-40f1-a560-ccea2e8950cb"> <br>

1. 서울시 열린데이터 광장에서 제공하는 api 를 통해 hotspot 50군데 장소에 대하여 5분간격으로 실시간데이터를 받습니다. <br> 
2. 받은 데이터를 3개의 파티션으로 구성된 seoulcity 토픽으로 프로듀싱 합니다. <br>
3. spark 같은 경우는 2개의 클러스터로 운용하였는데 , 하나는 컨테이너 내 로컬 , 하나는 (마스터노드 1대 워커노드 4대) 로 구성된 클러스터로  각각 1코어에 메모리 4G 식 할당시켰습니다. <br>
여기서 데이터 시각화에 필요한 형태로 데이터를 가공합니다. <br>
4. 이후 처리된 데이터를 seoulcity_visual 토픽으로 프로듀싱하고 , spark 로컬 클러스터 같은 경우는 mongodb로 seoulcity raw데이터를 적재 합니다. <br>
5. 로컬에 따로 consumer 를 두어서 seoulcity_visual 토픽에 대한 데이터를 받았고, folium 을 활용해서 실시간 정보가 포함된 지도를 만들고 flask 앱을 띄워서 파일을 렌더링하는 형식으로 프로젝트를 구성하였습니다. <br>
---

## Demo
영상 크기문제로 ... 유튜브에 업로드 하였습니다. <br>
https://youtu.be/5LiICZbOpNU 

## Visualization

### 실시간 도로소통 정보 
도로의 혼잡도, 도로명, 구간명 , 구간거리 , 평균속도에 대한 실시간 정보를 제공합니다. <br>
혼잡도의 경우는 색상에 따라 다른 정도를 나타냅니다. <br>
- red : 정체
- orange : 서행
- green : 원활 <br>
아래는 예시 그림입니다. <br>
<img width="573" alt="화면 캡처 2023-06-07 142635" src="https://github.com/siho-song/seoulcity-etl-pipeline/assets/79968994/ab24f828-ddb6-4438-976b-a83aa1cf8c4b"> <br>

---
### 실시간 주차장 정보
주차장명, 주소 , 주차가능수 , 가격에 대한 실시간 정보를 제공합니다. <br>
주차장의 경우 실시간정보를 제공하는 주차장도 있고, 제공하지 않는 주차장도 있습니다. <br>
실시간 정보를 제공하는 주차장<br> 
- red : 주차불가능
- green: 주차가능
<br>
실시간 정보를 제공하지 않는 주차장<br> 
-black <br>
아래는 예시 그림입니다. <br>
<img width="569" alt="화면 캡처 2023-06-07 142653" src="https://github.com/siho-song/seoulcity-etl-pipeline/assets/79968994/15c7d73d-3941-4aee-9380-40dec34b4482"> <br>

---
### 실시간 따릉이 정보
정류장명, 대여가능수, 반냡율에 대한 실시간 정보를 제공합니다 <br>
대여가능 수에 따라 다른 대여가능 수를 나타냅니다.<br>
- green : 4대 이상
- skyblue : 2대~4대
- orange : 1대~2대
- black : 대여 불가능
<br>


<img width="551" alt="화면 캡처 2023-06-07 142644" src="https://github.com/siho-song/seoulcity-etl-pipeline/assets/79968994/cb6df2d5-dada-4dc7-b1fa-c1083e058bea">



