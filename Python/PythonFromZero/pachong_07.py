from bs4 import BeautifulSoup
import requests

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}
url = 'http://www.infoq.com/news/'


def craw2(url):
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'lxml')
    print(response.text)

    for title_href in soup.find_all('div', class_='news_type_block'):
        print([title.get('title')
               for title in title_href.find_all('a') if title.get('title')])


craw2(url)
