import json
import time
import schedule
import xmltodict
import os
import requests
import pandas as pd
from kafka import KafkaProducer


def split_data(data, max_size):
    data_str = json.dumps(data,ensure_ascii=False)
    size = len(data_str)
    if size <= max_size:
        return [data_str]
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
    splits.append()
    return splits


    
def create_json_data(raw_data):\
    
    AREA_NM = raw_data["SeoulRtd.citydata"]["CITYDATA"]["AREA_NM"]
    PRK_STTS=raw_data["SeoulRtd.citydata"]["CITYDATA"]["PRK_STTS"]
    ROAD_TRAFFIC_STTS=raw_data["SeoulRtd.citydata"]["CITYDATA"]["ROAD_TRAFFIC_STTS"]
    SBIKE_STTS=raw_data["SeoulRtd.citydata"]["CITYDATA"]["SBIKE_STTS"]

    key_values = [
        ("AREA_NM", raw_data["SeoulRtd.citydata"]["CITYDATA"]["AREA_NM"]),
        ("ROAD_TRAFFIC_STTS", raw_data["SeoulRtd.citydata"]["CITYDATA"]["ROAD_TRAFFIC_STTS"]),
        ("PRK_STTS", raw_data["SeoulRtd.citydata"]["CITYDATA"]["PRK_STTS"]),
        ("SBIKE_STTS", raw_data["SeoulRtd.citydata"]["CITYDATA"]["SBIKE_STTS"])
]
    data = {key: value for key, value in key_values}

    json_data = json.dumps(data, ensure_ascii=False)

    return json_data
    