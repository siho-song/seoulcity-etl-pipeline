import json
import time
import schedule
import xmltodict
import os
import requests
import pandas as pd
from kafka import KafkaProducer


def split_data(data, max_size):
    data_str = json.dumps(data, indent=4,ensure_ascii=False)
    size = len(data_str)
    if size <= max_size:
        return [data]
    num_splits = (size + max_size - 1) // max_size
    split_size = size // num_splits
    splits = []
    for i in range(num_splits):
        start = i * split_size
        end = start + split_size
        if i == num_splits - 1:
            end = size
        split_data = data_str[start:end]
        splits.append(split_data)

    return splits

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer = lambda x: str(x).encode('utf-8')
                         )


def data_producing(API_KEY,hotspots_list):
    for i in hotspots_list:
        for j in i:
            url="http://openapi.seoul.go.kr:8088/"+API_KEY+"/XML/citydata/1/5/"+j
            res = requests.get(url)
            data=xmltodict.parse(res.content,encoding="utf-8")
            data_splits = split_data(data, max_size=100000) # 최대 크기 1MB로 설정
            metadatas=[]
            for split in data_splits:
                metadata = producer.send('seoulcity', split).get()
                metadatas.append((f"Message produced to partition {metadata.partition}, offset {metadata.offset}"))
                producer.flush()
                print(metadatas)
        time.sleep(10)
        

# path variable
kafka_home = os.getcwd()
dataset_path = kafka_home+"\\resource\\dataset\\"
file_hotspot = dataset_path+"seoulcity-hotspot.xlsx"

#environment variable
API_KEY= os.environ.get('SEOUL_SECRET_KEY')

hotspots = pd.read_excel(file_hotspot)
hotspots=hotspots['장소명']
hotspots_list=[]
for i in range(0,len(hotspots),5):
    hotspots_list.append(hotspots[i:i+5])
#               "강남 MICE 관광특구","동대문 관광특구","명동 관광특구","이태원 관광특구","잠실 관광특구","종로·청계 관광특구",
#                "홍대 관광특구","경복궁·서촌마을","광화문·덕수궁","창덕궁·종묘","가산디지털단지역","강남역","건대입구역",
#                "고속터미널역","교대역","구로디지털단지역","서울역","선릉역","신도림역","신림역","신촌·이대역","역삼역","연신내역"
#                ,"용산역","왕십리역","DMC(디지털미디어시티)","창동 신경제 중심지","노량진","낙산공원·이화마을","북촌한옥마을",
#                "가로수길","성수카페거리","수유리 먹자골목","쌍문동 맛집거리","압구정로데오거리","여의도","영등포 타임스퀘어","인사동·익선동",
#                "국립중앙박물관·용산가족공원","남산공원","뚝섬한강공원","망원한강공원","반포한강공원","북서울꿈의숲","서울대공원","서울숲공원",
#                "월드컵공원","이촌한강공원","잠실종합운동장","잠실한강공원"
# print(hotspots_list)
data_producing(API_KEY,hotspots_list)

# schedule.every(5).minute.do(data_producing)
  
# while 1:
#     schedule.run_pending()
#     time.sleep(10)