import requests
import sqlalchemy as db
import pandas as pd

url = 'http://apis.data.go.kr/1661000/FireInformationService/getOcByfrstFireSmrzPcnd'

params ={'serviceKey' : ' ' #보안키, 
         'pageNo' : '1', 
         'numOfRows' : '10', 
         'resultType' : 'json', 
         'ocrn_ymd' : '20201106'}

# 위에 작성한 url로 get요청을 보냄 
response = requests.get(url, params=params)

parseResponse = response.json()

# JSON의 응답에서 원하는 데이터만 추출하여 변수에 저장
data = parseResponse["response"]["body"]["items"]["item"]

fire = []

for item in data:
    dict = {}
    dict["FRST_CETR_NM"] = item["frstCetrNm"]
    dict["OCRN_YMD"] = item["ocrnYmd"]
    dict["SIDO_HQ_FRST_CERT_NM"] = item["sidoHqFrstCetrNm"]

    fire.append(dict)

print(fire)

# 데이터를 판다스로 변경
fire_df = pd.DataFrame(fire)
print(fire_df)

# csv 저장
fire_df.to_csv("fire.csv", index=False, encoding="UTF-8-sig");

# db연결
# mysql+pymysql://세션이름:세션비번@url:포트번호/db이름
engine= db.create_engine(f"mysql+pymysql://test:1234@127.0.0.1:3306/pythondb")

# DataFrame을 db의 fire 테이블에 저장
# 이미 테이블이 존재하면 덮어쓰기 함
fire_df.to_sql("fire",engine, index=False, if_exists="replace")

# sql문을 실행하여 데이터를 읽어와서 DataFrame으로 변환
fire_df_from_db = pd.read_sql("select * from fire", engine)

# 출력
print(fire_df_from_db)