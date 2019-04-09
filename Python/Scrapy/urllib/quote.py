from urllib.parse import quote, unquote

# quote将内容转化为URL编码的格式
# URL含有中文参数可能出现乱码时，可以将其转化成URL编码
keyword = '天堂'
url = 'https://www.baidu.com/s?wd=' + quote(keyword)
print(url)

# unquote对编码后的url进行解码
print(unquote(url))
