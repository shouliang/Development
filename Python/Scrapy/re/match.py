import re

content = 'Hello 123 4567 Word_This_is a Regex Demo'
print(len(content))

# match()会尝试从字符串的起始开始匹配，成功返回结果，否则返回None
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
print(result)
print(result.group())
print(result.span())