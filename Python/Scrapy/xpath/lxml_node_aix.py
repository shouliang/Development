# 节点轴选择
from lxml import etree

text = '''
<div>
<ul>
<li class="item0"><a href="link1.html"><span>first item</span></a></li>
<li class="item1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item1"><a href="link4.html">fourth item</a></li>
<li class="item0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
'''
html = etree.HTML(text)

# ancestor 获取所有祖先节点，需要两个冒号::,然后是节点选择器，直接使用*，匹配所有节点
result = html.xpath('//li[1]/ancestor::*')
print(result)

# 祖先节点中是div的节点
result = html.xpath('//li[1]/ancestor::div')
print(result)

# attribute获取节点属性，*表示获取所有属性
result = html.xpath('//li[1]/attribute::*')
print(result)

# child轴获取所有直接子节点
result = html.xpath('//li[1]/child::a[@href="link1.html"]')
print(result)

# descendant获取所有直接节点
result = html.xpath('//li[1]/descendant::span')
print(result)

# following获取当前节点之后的所有节点
result = html.xpath('//li[1]/following::*[2]')
print(result)

# following-sibling获取当前节点之后的所有同级节点
result = html.xpath('//li[1]/following-sibling::*')
print(result)
