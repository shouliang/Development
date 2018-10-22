from lxml import etree

text = '''
<li class="li li-first" name="item"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[@class="li"]/a/text()')
print(result)

# 属性多值获取，需要用到contain函数
result = html.xpath('//li[contains(@class, "li")]/a/text()')
print(result)

# 多属性匹配，用and操作符连接，需要同时满足
result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
print(result)


