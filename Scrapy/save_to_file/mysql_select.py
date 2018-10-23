import pymysql

db = pymysql.connect(host='192.168.19.100', user='dxl_dev', password='zeek9Ahr', port=3306, db='spiders')
cursor = db.cursor()
sql = 'SELECT * FROM students WHERE age >= 20'
try:
    cursor.execute(sql);
    print('Count: ', cursor.rowcount)

    # 获取第一条数据
    one = cursor.fetchone()
    print('One:', one)

    # fetchall()方法不是获取所有
    # 因为fetchone后游标指针已经偏移到下一条数据
    # fetchall()获取所有数据，以元组形式返回
    # 如果数据量比较大，暂用内存开销会比较高
    results = cursor.fetchall()
    print('Results:', results)

    print('Results Type:', type(results))
    for row in results:
        print(row)
except:
    print('Failed')

db.close()
