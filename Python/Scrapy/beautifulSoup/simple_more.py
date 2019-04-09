from bs4 import BeautifulSoup

html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dormouse"><b> The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http:example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http:example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http:example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p> 
'''

# 指定lxml为解析器
soup = BeautifulSoup(html, 'lxml')

# 以标准的缩进格式输出解析后的字符串
# print(soup.prettify())

print(soup.title)

# 类型为：bs4.element.Tag
print(type(soup.title))

# 提取title节点中的文本内容
print(soup.title.string)
print(soup.head)

# 注意：只会选择发现结果中的第一个p节点的内容
print(soup.p)


# 获取节点名称
print(soup.title.name)

# 获取属性：通过attrs获取，返回字典
print(soup.p.attrs)
print(soup.p.attrs['name'])

# 获取属性，也可直接传入属性名来获取
print(soup.p['name'])
print(soup.p['class'])

# 获取内容： 利用string获取节点包含的文本内容
print(soup.p.string)

# 嵌套选择：通过多次.的形式
print(soup.head.title.string)
