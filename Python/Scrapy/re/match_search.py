import re

# match方法从字符串开头开始匹配，一旦开头不匹配，整个匹配就失败了
# search方法会扫描整个字符串，然后返回第一个成功匹配的结果
content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
# result = re.match('Hello.*?(\d+).*?Demo', content)
result = re.search('Hello.*?(\d+).*?Demo', content)
print(result)
