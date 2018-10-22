import re

content = '''Hello 1234567 World_This_is 
a Regex Demo
'''
# result = re.match('^Hello.*?(\d+).*Demo$', content)

# 加了个修饰符re.S,使.(点)可以匹配包括换行符在内的所有字符
result = re.match('^Hello.*?(\d+).*Demo$', content, re.S)
print(result)
print(result.group(1))
