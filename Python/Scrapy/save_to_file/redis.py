from redis import StrictRedis

# 连接redis
redis = StrictRedis(host='127.0.0.1', port=6379, db=0, password='')

# 设置键值
redis.set('name', 'liang')

# 获取键值
print(redis.get('name'))