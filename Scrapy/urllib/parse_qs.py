from urllib.parse import parse_qs, parse_qsl

# parse_qs将一串GET请求参数转回字典
query = 'name=germey&age=22'
print(parse_qs(query))

# parse_qsl将参数转化为元组组成的列表
print('--------------------')
print(parse_qsl(query))
