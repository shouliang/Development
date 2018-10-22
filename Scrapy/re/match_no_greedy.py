import re

# 加了个问号?,变成非贪婪匹配：尽可能匹配少的字符
content = 'Hello 1234567 World_This_is a Regex Demo'
result = re.match('^Hello.*?(\d+).*Demo$', content)
print(result)
print(result.group(1))
