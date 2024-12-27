import sys
import mariadb

# db를 연결하기 위한 mariaDbConnection 함수 생성
def mariaDbConnection(u, pw, h, p, d):
    try:
        # 유저, 비밀번호, 호스트, 포트번호, 데이터베이스 이름을 설정함
        conn = mariadb.connect(user = u, password = pw, host = h, port = p, database = d)
        # 연결에 성공하면 아래 문장을 리턴
        print("DB Connection Success: {0}".format(h))
    except mariadb.Error as e:
        # 에러가 발생하면 아래 문장을 리턴
        print("Error connecting to MariaDB Platform : {}".format(e))
        sys.exit(1)
    
    return conn
 
# db 연결을 종료하기 위한 함수 생성
def mariaDbClose(c):
    try:
        # 닫기에 성공하면 아래 문장을 리턴
        c.close()
        print("DB Close Success")
    except mariadb.Error as e:
        # 에러가 발생하면 아래 문장을 리턴
        print("Error closing from MariaDB Platform")
        sys.exit(1)