import pandas as pd
import mariadbQuery

# mariadbQuery파일에서 참조하여 연결한 db에 연결
dbConn = mariadbQuery.mariaDbConnection('seatest', '1234', '127.0.0.1', 3306, 'seadisaster')
cur = dbConn.cursor()

# 엑셀 데이터를 읽어옴
readData = pd.read_excel("국내해양사고통계추출(진짜 최종).xlsx")

# 가져온 데이터를 쿼리문을 작성하여 db에 연결하고
# 각 테이블에 필요한 데이터를 삽입함

# Accident_status (해양사고 발생 현황) 테이블
for i in readData.index:
    query = "INSERT INTO accident_status(accident_num, name, type, ton, kind) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')".format(i+1,
                                                                                                                                 readData['사건명'][i],
                                                                                                                                 readData['해양사고종류1'][i],
                                                                                                                                 readData['톤수범위(통계용)'][i],
                                                                                                                                 readData['선박용도(통계용)'][i])
    cur.execute(query)
dbConn.commit()

# Accidents_Time(사고 발생 시간) 테이블
for i in readData.index:
    query = "CALL insert_at_id_proc('{0}', '{1}', '{2}', '{3}')".format(i+1,
                                                                        readData['해양사고발생시간'][i],
                                                                        readData['해양사고발생시간대'][i],
                                                                        readData['계절'][i])
    cur.execute(query)
dbConn.commit()

# Accidents_Damage(사고 인명 피해) 테이블
for i in readData.index:
    query = "CALL insert_ad_id_proc('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')".format(i+1,
                                                                                      readData['사망합계(선원+여객+기타)'][i],
                                                                                      readData['실종합계(선원+여객+기타)'][i],
                                                                                      readData['인명피해합계(사망+실종)'][i],
                                                                                      readData['부상합계(선원+여객+기타)'][i],
                                                                                      readData['총합(사망+실종+부상)'][i])
    cur.execute(query)
dbConn.commit()

# Accidents_location (사고 발생 위치) 테이블
for i in readData.index:
    query = "CALL insert_al_id_proc('{0}', '{1}', '{2}', '{3}')".format(i+1,
                                                                        readData['해양사고발생지역(통계용)'][i],
                                                                        readData['위도'][i],
                                                                        readData['경도'][i])
    cur.execute(query)
dbConn.commit()

# db닫기
mariadbQuery.mariaDbClose(dbConn)