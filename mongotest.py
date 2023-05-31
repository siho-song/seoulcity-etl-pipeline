from pymongo import MongoClient

# MongoDB에 접속
client = MongoClient('mongodb://show:gkdldhdl@localhost:27017')

# 데이터베이스 선택
db = client.seoulcity

# 삽입할 데이터 생성
data = {
    'name': 'John',
    'age': 30,
    'city': 'Seoul'
}

# 컬렉션 선택 (없는 경우 자동으로 생성됨)
collection = db.test

# 데이터 삽입
insert_result = collection.insert_one(data)

# 삽입된 데이터의 _id 출력
print(f"Inserted data ID: {insert_result.inserted_id}")