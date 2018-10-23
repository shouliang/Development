import requests
from pyquery import PyQuery as pq

# 知乎热门话题
url = 'https://www.zhihu.com/explore'

# 伪造User-Agent，防止被反爬
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
# 使用requests获取html
html = requests.get(url, headers=headers).text
# 使用pyquery解析html
doc = pq(html)

items = doc('.explore-tab .feed-item').items()
for item in items:
    # 标题
    question = item.find('h2').text()
    # 作者
    author = item.find('.author-link-line').text()
    # 内容
    answer = pq(item.find('.content').html()).text()

    # a 代表以追加的方式写入到文本，指定编码为utf-8
    file = open('explore.txt', 'a', encoding='utf-8')
    file.write('\n'.join([question, author, answer]))
    # 每个热门话题以50个等号的形式分割
    file.write('\n' + '=' * 50 + '\n')
    file.close()

    # 一种写入文件的简写，使用with as，这样就不用显示关闭文件了
    with open('explore.txt', 'a', encoding='utf-8') as file:
        file.write('\n'.join([question, author, answer]))
        file.write('\n' + '=' * 50 + '\n')
