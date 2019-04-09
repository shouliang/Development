import pymysql

# 插入数据
id = '20120001'
user = 'Bob'
age = 20

db = pymysql.connect(host='192.168.19.100', user='dxl_dev', password='zeek9Ahr', port=3306, db='spiders')
cursor = db.cursor()

sql = "INSERT INTO students(id, name, age) values (%s, %s, %s)"
try:
    # 参数通过元组来传递，避免了字符串拼接的麻烦
    cursor.execute(sql, (id, user, age))
    # 执行commit()方法才可实际插入数据，这个方法才是真正将语句提交到数据库执行的方法
    db.commit()
    print('insert data successful ha')
except:
    db.rollback()
db.close()
