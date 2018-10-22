from bs4 import BeautifulSoup

# Beautiful Soup在解析时实际上要依赖解析器
# 如：第三方解析器lxml
soup = BeautifulSoup('<p>Hello<p>', 'lxml')

print(soup.p.string)