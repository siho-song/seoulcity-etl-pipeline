from kafka import KafkaConsumer
import time
import json
import folium

consumer = KafkaConsumer(
    'seoulcity',  # 수신할 토픽명
    bootstrap_servers='localhost:9092',
    auto_offset_reset='latest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)


for message in consumer:
    
    
    data = message.value
    print(data)