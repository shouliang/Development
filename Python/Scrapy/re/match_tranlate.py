import re

# 转义字符，在前面加反斜线转义即可
content = '(百度)www.baidu.com'
result = re.match('\(百度\)www\.baidu\.com', content)
print(result)