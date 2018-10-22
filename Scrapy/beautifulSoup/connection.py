from bs4 import BeautifulSoup

html = '''
<html><head>
<title>The Dormouse's story</title>
</head>
<body>
<p class="story">
    Once upon a time there were three little sisters; and their names were
    <a href="http:example.com/elsie" class="sister" id="link1">
<span>Elsie</span>
</a>
<a href="http:example.com/lacie" class="sister" id="link2">Lacie</a> 
and
<a href="http:example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.
</p>
<p class="story">...</p> 
'''

# 指定lxml为解析器
soup = BeautifulSoup(html, 'lxml')

# contents获取直接子节点
print(soup.p.contents)

# 遍历所有p节点下的直接子节点，通过children属性来实现
for i, child in enumerate(soup.p.children):
    print(i, child)

print('---------------------- for in descendant ----------------------')
# 遍历子孙节点，通过descendants属性来实现
print(soup.p.descendants)
for i, child in enumerate(soup.p.descendants):
    print(i,child)

# 获取父节点:通过parent属性
print(soup.a.parent)

# 获取祖先点:通过parents属性
print(soup.a.parents)
