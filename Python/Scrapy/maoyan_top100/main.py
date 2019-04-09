import json
import requests
from requests.exceptions import RequestException
import re
import time

# 请求并返回html
def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


# 解析页面html，将结果让放入字典中
def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)

    # 正则匹配后找到所有结果，遍历后放入字典中
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6],
        }


# 将解析后的结果写入文件(每次写入单条记录)
def write_to_json(content):
    with open('result.txt', 'a') as f:
        print(type(json.dumps(content)))

        # JSON库的dumps实现字典的序列化
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


# 构造通用的分页抓取函数(每次只抓取一页)
def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_json(item)


# 遍历10页
if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
        # 延时一秒后再抓取后面页的结果，防止速度过快被反爬虫
        time.sleep(1)
