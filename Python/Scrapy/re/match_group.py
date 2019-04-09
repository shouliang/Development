import re

content = 'Hello 1234567 World_This is a Regex Demo'

# 使用()括号将想提取的字符串括起来
result = re.match('^Hello\s(\d+)\sWorld', content)
print(result)
print(result.group())

# group(1)提取出匹配的结果
print(result.group(1))
print(result.span())