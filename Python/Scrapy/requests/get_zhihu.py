import requests
import re

# 构造头部，通过User-Agent字段来包含浏览器的标识信息
# 如果不加头部，知乎会禁止抓取
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
# 抓取网页
r = requests.get('https://www.zhihu.com/explore', headers=headers)

# 用正则表达式匹配出需要的内容
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
titles = re.findall(pattern, r.text)
print(titles)

print('no headers')
r = requests.get('https://www.zhihu.com/explore')
print(r.text)
