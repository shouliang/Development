import pymysql

db = pymysql.connect(host='192.168.19.100', user='dxl_dev', password='zeek9Ahr', port=3306)
# 获取游标
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
# 获取第一条数据，也就得到了版本号
data = cursor.fetchone()
print('Database version:', data)
cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
db.close()
