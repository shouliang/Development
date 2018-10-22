import requests

r = requests.get('https://www.baidu.com')
print(r.cookies)

# 遍历cookies.items
for key, value in r.cookies.items():
    print(key + '=' + value)
