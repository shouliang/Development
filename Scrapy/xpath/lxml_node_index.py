# 按序选择
from lxml import etree

text='''
<div>
<ul>
<li class="item0"><a href="link1.html">first item</a></li>
<li class="item1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item1"><a href="link4.html">fourth item</a></li>
<li class="item0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
'''
html = etree.HTML(text)

# 通过索引来获取，索引从1开始
result = html.xpath('//li[1]/a/text()')
print(result)

result = html.xpath('//li[last()]/a/text()')
print(result)

result = html.xpath('//li[position() < 3]//text()')
print(result)

result = html.xpath('//li[last() - 2]//text()')
print(result)