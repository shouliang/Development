import re

content = 'Hello 1234567 World_This_is a Regex Demo'
result = re.match('^Hello.*?(\d+).*Demo$', content)
print(result)
print(result.group(1))