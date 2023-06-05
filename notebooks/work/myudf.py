def rts_preprocessing(ROAD_TRAFFIC_STTS):
    result=[]
    for element in ROAD_TRAFFIC_STTS:
        extracted_data = {
            "ROAD_NM": element.ROAD_NM,
            "START_ND_NM": element.START_ND_NM,
            "END_ND_NM": element.END_ND_NM,
            "DIST": element.DIST,
            "SPD": element.SPD,
            "IDX": element.IDX,
            "XYLIST": element.XYLIST
        }
        result.append(extracted_data)
    return result
    
    
def prks_preprocessing(PRK_STTS):
    result=[]
    for element in PRK_STTS:
        extracted_data = {
            "PRK_NM": element.PRK_NM,
            "CPCTY": element.CPCTY,
            "CUR_PRK_CNT": element.CUR_PRK_CNT,
            "CUR_PRK_TIME": element.CUR_PRK_TIME,
            "CUR_PRK_YN": element.CUR_PRK_YN,
            "PAY_YN": element.PAY_YN,
            "RATES": element.RATES,
            "TIME_RATES": element.TIME_RATES,
            "ADD_RATES": element.ADD_RATES,
            "ADD_TIME_RATES": element.ADD_TIME_RATES,
            "ADDRESS": element.ADDRESS,
            "ROAD_ADDR": element.ROAD_ADDR,
            "LNG": element.LNG,
            "LAT": element.LAT
        }
        result.append(extracted_data)
    return result
    
    
    
def sbikes_preprocessing(SBIKE_STTS):
    result=[]
    for element in SBIKE_STTS:
        extracted_data = {
            "SBIKE_SPOT_NM": element.SBIKE_SPOT_NM,
            "SBIKE_SHARED": element.SBIKE_SHARED,
            "SBIKE_PARKING_CNT": element.SBIKE_PARKING_CNT,
            "SBIKE_RACK_CNT": element.SBIKE_RACK_CNT,
            "SBIKE_X": element.SBIKE_X,
            "SBIKE_Y": element.SBIKE_Y
        }
        result.append(extracted_data)
    return result
    