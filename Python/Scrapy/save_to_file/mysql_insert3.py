import pymysql

# 通过构造字典来实现较为通用的插入数据,字典中的key为数据库表中的字段名称
data = {
    'id': '20120002',
    'name': 'zhangsan111',
    'age': 21
}

table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s'] * len(data))

# ON DUPLICATE KEY UPDATE ,表示如果主键已经存在，则执行更新操作
sql = "INSERT INTO {table}({keys}) values ({values}) ON DUPLICATE KEY UPDATE".format(table=table, keys=keys,
                                                                                     values=values)
update = ','.join([" {key} = %s".format(key=key) for key in data])
sql += update

db = pymysql.connect(host='192.168.19.100', user='dxl_dev', password='zeek9Ahr', port=3306, db='spiders')
cursor = db.cursor()

try:
    if cursor.execute(sql, tuple(data.values()) * 2):
        print('Successful')
        db.commit()
except:
    print('Failed')
    db.rollback()
db.close()
