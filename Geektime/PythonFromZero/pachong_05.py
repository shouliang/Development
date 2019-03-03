import requests
import re

url = 'http://www.cnu.cc/discoveryPage/hot-人像'
content = requests.get(url).text
# print(content)

pattern = re.compile(r'<a href="(.*?)".*?title">(.*?)</div>', re.S)
results = re.findall(pattern, content)
# print(results)

for result in results:
    url, name = result
    print(url, re.sub('\s', '', name))
