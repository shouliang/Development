import re

# 通用匹配： .(点)可以匹配任意字符(除换行符)，*(星)代表匹配的前面的字符无限次
# 所以它们组合到一起就可以匹配任意字符
content = 'Hello 123 4567 World_This_is a Regex Demo'
result = re.match('^Hello.*Demo$', content)
print(result)
print(result.group())
print(result.span())
