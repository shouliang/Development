import pymysql

# 通过构造字典来实现较为通用的插入数据,字典中的key为数据库表中的字段名称
data = {
    'id': '20120002',
    'name': 'zhangsan',
    'age': 21
}

table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s'] * len(data))
sql = "INSERT INTO {table}({keys}) values ({values})".format(table=table, keys=keys, values=values)

db = pymysql.connect(host='192.168.19.100', user='dxl_dev', password='zeek9Ahr', port=3306, db='spiders')
cursor = db.cursor()

try:
    # 参数通过元组来传递
    if cursor.execute(sql, tuple(data.values())):
        print('Successful')
        db.commit()
except:
    print('Failed')
    db.rollback()
db.close()
