from bs4 import BeautifulSoup

html_doc = ""
soup = BeautifulSoup(html_doc, 'lxml')

print(soup.prettify())
print(soup.title)


# 找出p标签
print(soup.p)


