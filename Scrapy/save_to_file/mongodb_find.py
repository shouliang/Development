import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
collection = db.students

# 查询
result = collection.find_one({'name': 'Merry'})
print(type(result))
print(result)

# 查询：返回结果多条
results = collection.find({'age':{'$gt': 20}})
print(results)
for result in results:
    print(result)

print('------ regex ------')
# 也可以正则匹配
results = collection.find({'name':{'$regex': '^M.*'}})
for result in results:
    print(result)