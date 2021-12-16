import mysql.connector
from datetime import datetime
# 여러개의 데이터를 집어 넣는 경우 
try:
    # 1. DB에 연결
    connection = get_connection()
    # 2. 쿼리문 만들기
    current_time = datetime.now()

    query = '''insert into test
                (name,date)
                values
                (%s,%s); '''
    # 파이썬에서, 튜플만들때, 데이터가 1개인 경우에는, 
    # 콤마, 꼭 써준다.
    record=[('qqq',current_time),('yyy',current_time),('ppp',current_time)]
    # 3. 커넥션으로부터 커서를 가져온다.
    cursor = connection.cursor()

    # 4. 쿼리문을 커서에 넣어서 실행한다.
    cursor.executemany(query,record)

    # 5. 커넥션을 커밋한다. => 디비(DB)에 영구적으로 반영하라는 뜻
    connection.commit()

except mysql.connector.errors as e:
    print('Error',e )
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print('MYSQL connection is  closed')
