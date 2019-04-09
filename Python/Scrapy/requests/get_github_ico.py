import  requests

# 抓取二进制数据
r = requests.get('https://github.com/favicon.ico')

# 由于图片是二进制数据，所以在转换成str类型后，会出现乱码
print(r.text)
print(r.content)

# w:write b(binary),以二进制写的方式打开文件
with open('favicon.ico', 'wb') as f:
    f.write(r.content)