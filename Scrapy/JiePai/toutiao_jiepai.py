import requests
from urllib.parse import urlencode
from requests import codes
import os
from hashlib import md5
from multiprocessing.pool import Pool


# 加载单个Ajax请求的结果
def get_page(offset):
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab'
    }
    base_url = 'http://www.toutiao.com/search_content/?'
    url = base_url + urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None


# 解析json中的图片，放入一个生成器
def get_iamges(json):
    if json.get('data'):
        data = json.get('data')
        for item in data:
            if item.get('cell_type') is not None:
                continue
            title = item.get('title')
            images = item.get('image_list')
            for image in images:
                yield {
                    'image': 'https:' + image.get('url'),
                    'title': title
                }


# 保存图片
def save_image(item):
    img_path = item.get('title')
    # 创建文件夹: 用title命名
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    try:
        resp = requests.get(item.get('image'))
        if codes.ok == resp.status_code:
            # 构造file_path
            file_path = '{img_path}/{file_name}.{file_stuffx}'.format(
                img_path=img_path,
                file_name=md5(resp.content).hexdigest(),
                file_stuffx='jpg'
            )
            # 写入文件
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(resp.content)
                print('Downloaded image path is %s' % file_path)
            else:
                print('Already Downloaded', file_path)

    except requests.ConnectionError:
        print('Failed to Save Image, item %s' % item)


def main(offset):
    json = get_page(offset)
    for item in get_iamges(json):
        print(item)
        save_image(item)


GROUP_START = 0
GROUP_END = 7

if __name__ == '__main__':
    # 线程池
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    # map方法实现多线程下载
    pool.map(main, groups)
    pool.close()
    pool.join()
