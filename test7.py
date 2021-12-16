import mysql.connector

# update 하는법 데이터 바꾸기
try:
    # 1. DB에 연결
    connection = get_connection()
    name = '미애'
    id = 6
    # date = '2021-12-15'
    # 2. 쿼리문 만들기
    query = '''update test
            set name = %s
            where id = %s; '''
    # 파이썬에서, 튜플만들때, 데이터가 여러개인 경우에는, 
    # 콤마, 꼭 써준다.
    record=[('홍길동',2),('김길동',4),('이길동',7)]
    # 3. 커넥션으로부터 커서를 가져온다.
    cursor = connection.cursor()

    # 4. 쿼리문을 커서에 executemany을 사용 넣어서 실행한다.
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
