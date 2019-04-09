html = '''
<div class="wrap">
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
</div>
'''

from pyquery import PyQuery as pq

doc = pq(html)

# 子节点
items = doc('.list')
print(type(items))
print(items)

# 这里的find方法的查找范围是所有的子孙节点
lis = items.find('li')
print(type(lis))
print(lis)

# 如果只有查找子节点，可以使用children()方法
print('------ children ------')
lis = items.children()
print(type(lis))
print(lis)

# 筛选特定节点
lis = items.children('.active')
print(lis)

# 父节点
print('------ parent ------')
items = doc('.list')
container = items.parent()
print(type(container))
print(container)

# 祖先节点
print('------ parents ------')
items = doc('.list')
parents = items.parents()
print(type(parents))
print(parents)

# 过滤祖先节点
print('------ parents filter ------')
parents = items.parents('.wrap')
print(type(parents))
print(parents)

# 兄弟节点
print('------ siblings ------')
li = doc('.list .item-0.active')
print(li.siblings())

# 兄弟节点-之过滤
print('------ siblings  filter------')
li = doc('.list .item-0.active')
print(li.siblings('.active'))

# 遍历 items()
print('------ for in items------')
lis = doc('li').items()
print(type(lis))
for li in lis:
    print(li, type(li))

# 获取属性
print('------ get attribute ------')
a = doc('.item-0.active a')
print(a, type(a))
# 以下获取属性的两种方法，效果是一样的
print(a.attr('href'))
print(a.attr.href)

# 遍历 获取属性，还是通过items()
print('------ attribute items ------')
a = doc('a')
for item in a.items():
    print(item.attr('href'))

# 获取文本
print('------ text() ------')
a = doc('.item-0.active a')
print(a)
print(a.text())

# 获取html
print('------ html() ------')
li = doc('.item-0.active')
print(li)
# 获取li内部包含的html
print(li.html())

# 如果我们选中的是多个节点，html()返回第一个，text()则返回全部,中间用一个空格割开
print('------ multi node get html() and text()')
li = doc('li')
print(li.html())
print(li.text())