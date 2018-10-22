from lxml import etree

# 解析hmtl文件，会多出DOCTYPE的声明
html = etree.parse('./test.html', etree.HTMLParser())
result = etree.tostring(html)
print(result.decode('utf-8'))
