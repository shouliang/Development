import pymongo

# 连接MongoDB:两种方式均可
client = pymongo.MongoClient(host='localhost', port=27017)
# client = pymongo.MongoClient('mongodb://localhost:27017')

# 指定数据库:两种方式均可
db = client.test
# db = client['test]

# 指定集合，类似关系型数据库中的表
collection = db.students

# 插入数据：PyMongo 3.x版本中推荐使用 insert_one 或者 insert_many()
student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

# 插入一条数据:insert_one
# result = collection.insert(student)
# result = collection.insert_one(student)
# print(result)

# 插入多条数据:insert_many
student1 = {
    'id': '20170102',
    'name': 'Merry',
    'age': 23,
    'gender': 'female'
}

student2 = {
    'id': '20170103',
    'name': 'Tom',
    'age': 21,
    'gender': 'male'
}
result = collection.insert_many([student1, student2])
