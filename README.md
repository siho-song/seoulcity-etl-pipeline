
# seoulcity-etl-pipeline 
### 서울 열린데이터 광장 open api 를 활용한 etl pipeline 구축 및 시각화 프로젝트
---

## Version
OS : ubuntu:22.04 <br>
JDK : java-8-openjdk-amd64 <br>
Python : python3.10 <br>
Kafka : kafka_2.13-2.7.2 <br>
Spark : spark_3.4.0 <br>



---
## Architecture
<img width="945" alt="화면 캡처 2023-06-07 142602" src="https://github.com/siho-song/seoulcity-etl-pipeline/assets/79968994/2d152193-eae0-40f1-a560-ccea2e8950cb"> <br>

1. 서울시 열린데이터 광장에서 제공하는 api 를 통해 hotspot 50군데 장소에 대하여 5분간격으로 실시간데이터를 받습니다. <br> 
2. 받은 데이터를 3개의 파티션으로 구성된 seoulcity 토픽으로 프로듀싱 합니다. <br>
3. spark 같은 경우는 2개의 클러스터로 운용하였는데 , 하나는 컨테이너 내 로컬 , 하나는 (마스터노드 1대 워커노드 4대) 로 구성된 클러스터로  각각 1코어에 메모리 4G 식 할당시켰습니다. <br>
여기서 데이터 시각화에 필요한 형태로 데이터를 가공합니다. <br>

4.이후 처리된 데이터를 seoulcity_visual 토픽으로 프로듀싱하고 , spark 로컬 클러스터 같은 경우는 mongodb로 seoulcity raw데이터를 적재 합니다. <br>
5.로컬에 따로 consumer 를 두어서 seoulcity_visual 토픽에 대한 데이터를 받았고, folium 을 활용해서 실시간 정보가 포함된 지도를 만들고 flask 앱을 띄워서 파일을 렌더링하는 형식으로 프로젝트를 구성하였습니다. <br>





