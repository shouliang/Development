from urllib import request

url = 'http://www.baidu.com'
response = request.urlopen(url, timeout=1)
html = response.read().decode('utf-8')
print(html)

