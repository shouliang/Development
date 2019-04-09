from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())

# *表示匹配所有节点
result = html.xpath('//*')
print(result)

# 匹配所有的li节点
result = html.xpath('//li')
print(result)

# 匹配子节点
# /  用于选取直接子节点
# // 用于选取所有子孙节点
result = html.xpath('//li/a')
print(result)

# 直接选取ul的a节点，但实际上没有，故为空
result = html.xpath('//ul/a')
print(result)

result = html.xpath('//ul//a')
print(result)

# 父节点
result = html.xpath('//a[@href="link4.html"]/../@class')
print(result)

result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
print(result)

# 属性匹配
result = html.xpath('//li[@class="item-0"]')
print(result)

# 文本获取
result = html.xpath('//li[@class="item-0"]/text()')
print(result)

result = html.xpath('//li[@class="item-0"]/a/text()')
print(result)

result = html.xpath('//li[@class="item-0"]//text()')
print(result)

# 属性获取，此处是获得节点的某个属性值，区别于通过属性获取节点
result = html.xpath('//li/a/@href')
print(result)