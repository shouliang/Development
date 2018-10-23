import json

# JSON字符串中的数据需要用双引号来包围
str = '''
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
},{
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-09-05"
}]
'''

print(type(str))
# loads 将JSON字符串转换为JSON对象
data = json.loads(str)
print(data)

# 由于最外层是中括号，所以最终类型是列表类型
print(type(data))

print(data[0]['name'])
print(data[1]['birthday'])

# get方法，当键名不存在时，不会报错，会返回None
print(data[0].get('name'))
print(data[1].get('birthday'))

print('------ 从文件读取JSON ------')
with open('data.json', 'r') as file:
    str = file.read()
    data = json.loads(str)
    print(data)

print('------ 写入JSON到文件 ------')
data = [{
    "name": "王伟",
    "gender": "男",
    "birthday": "1993-11-25"
}]

# ensure-ascii为False,可以输出中文
with open('data2.json', 'w') as file:
    file.write(json.dumps(data, indent=2, ensure_ascii=False))
