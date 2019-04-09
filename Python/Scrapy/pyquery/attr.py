html = '''
<ul class="list">
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
</ul>
'''

from pyquery import PyQuery as pq
doc = pq(html)
li = doc('.item-0.active')
print(li)

# 设置属性
li.attr('name','link')
print(li)

# 修改文本
li.text('changed item')
print(li)

# 设置html
li.html('<span>changed item</span>')
print(li)