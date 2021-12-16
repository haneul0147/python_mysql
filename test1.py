import mysql.connector
from mysql.connector.errors import Error

# 연결하는 코드
# try 라고 나오면, 들여쓰기 되어있는 문장들을 실행하라는 뜻
try :
    connection = get_connection()
    if connection.is_connected():
        df_info = connection.get_server_info()
        print('MYSQL info', df_info)
# 위에 코드를 실행하다가 ,문제가 생기면, except 를 실행하라는 뜻
except Error as e:
    print('Error while connecting to MYSQL',e)
# finally 는 try에서 에러가 나든 안나든, 무조건 실행하라는 ㄸ,ㅅ/
finally:
    print('finally')
    if connection.is_connected():
        connection.close()
        print('MYSQL connection is closed')
    else :
        print('connection does not exist')
    
# try, except 는 같이 있어야 되고 
# finally 는 굳이 있을 필요 없다.