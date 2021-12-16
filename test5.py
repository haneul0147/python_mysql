import mysql.connector
from mysql.connector.errors import Error

# 연결하는 코드
# try 라고 나오면, 들여쓰기 되어있는 문장들을 실행하라는 뜻
try :
    connection = mysql.connector.connect(
        host='s.amazonaws.com',
        database = 'streamlit_db',
        user = 'python_user',
        password = '2105'
    )
   
    query = '''select * from test;'''
    # 셀렉트 결과를 딕셔너리로 가져오는 경우
    cursor = connection.cursor(dictionary = True)
    cursor.execute(query)
    
    # select 문은 아래 내용이 필요하다.
    record_list = cursor.fetchall()
    print(record_list)

    for row in record_list:
        print('id=',row['id'])
        print('name =',row['name'])
        print('date =',row['date'].isoformat())
# 위에 코드를 실행하다가 ,문제가 생기면, except 를 실행하라는 뜻
except Error as e:
    print('Error while connecting to MYSQL',e)
# finally 는 try에서 에러가 나든 안나든, 무조건 실행하라는 ㄸ,ㅅ/
finally:
    print('finally')
    cursor.close()
    if connection.is_connected():
        connection.close()
        print('MYSQL connection is closed')
    else :
        print('connection does not exist')