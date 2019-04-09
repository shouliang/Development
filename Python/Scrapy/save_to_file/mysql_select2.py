import pymysql

db = pymysql.connect(host='192.168.19.100', user='dxl_dev', password='zeek9Ahr', port=3306, db='spiders')
cursor = db.cursor()
sql = 'SELECT * FROM students WHERE age >= 20'
try:
    cursor.execute(sql);
    print('Count: ', cursor.rowcount)

    row = cursor.fetchone()
    # 逐条取数据
    while row:
        print('Row: ', row)
        row = cursor.fetchone()
except:
    print('Error')

db.close()
