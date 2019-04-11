from lxml import etree
text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''
# HTML文本中最后一个li节点没有闭合，但是etree模块可以自动修复HTML文本
html = etree.HTML(text)
result = etree.tostring(html)
print(result.decode('utf-8'))