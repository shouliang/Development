import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
collection = db.students

# 计数
count = collection.count_documents({'age': 21})
print(count)

# 排序
results = collection.find().sort('name', pymongo.ASCENDING)
print([result['name'] for result in results])

# 偏移
results = collection.find().sort('name', pymongo.ASCENDING).skip(1)
print([result['name'] for result in results])

# limit 限制返回个数
results = collection.find().sort('name', pymongo.ASCENDING).skip(1).limit(1)
print([result['name'] for result in results])

# 更新
condition = {'name': 'Merry'}
student = collection.find_one(condition)
result = collection.update_one(condition, {'$set': {'age': 26}})
print(result)
# 获取匹配的数据条数和影响的数据条数
print(result.matched_count, result.modified_count)

# 删除 delete_one and delete_many
result = collection.delete_one({'name':'Kevin'})
print(result)
print(result.deleted_count)
result = collection.delete_many({'age': {'$gt': 26}})
print(result.deleted_count)




