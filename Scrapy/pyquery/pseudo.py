html = '''
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
'''

# 伪类选择器
from pyquery import PyQuery as pq

doc = pq(html)
li = doc('li:first-child')
print(li)

li = doc('li:last-child')
print(li)

# li中索引为2的节点，索引从0开始
li = doc('li:nth-child(2)')
print(li)

li = doc('li:gt(2)')
print(li)

# 偶数位置的节点
li = doc('li:nth-child(2n)')
print(li)

# 包含second文本的节点
li = doc('li:contains(second)')
print(li)
