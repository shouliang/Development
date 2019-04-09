import pymysql

db = pymysql.connect(host='192.168.19.100', user='dxl_dev', password='zeek9Ahr', port=3306, db='spiders')
# 获取游标
cursor = db.cursor()
# 创建表的sql语句
sql = 'CREATE TABLE IF NOT EXISTS students( id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY(id))'
cursor.execute(sql)
db.close()
