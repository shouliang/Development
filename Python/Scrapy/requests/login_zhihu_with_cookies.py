import requests

# 直接copy登录知乎网站后产生的cookie字段来模拟登录
headers = {
    'Cookie': 'tgw_l7_route=5bcc9ffea0388b69e77c21c0b42555fe;'
              '_xsrf=YexaZGfEwWnCZmkGIhjw4pF7FlY5CZEu;'
              '_zap=50872d8d-0e4d-4414-b90b-e5b155e09577;'
              'd_c0="AIAnv7t5WA6PTpdA1tLalvu1cyvaKHCMRbg=|1539235660";'
              'q_c1=4f9499bd061a4e498940ed51729bf3e3|1539235674000|1539235674000;'
              'capsion_ticket="2|1:0|10:1539235746|14:capsion_ticket|44:ZGZmY2NjMzYzMTMxNDgzMjg5MDMxODRkM2MxMGJhOGU=|ea0a4fb7cc920be137e42745fc2be2aebc1af58066f52c7175ab64ac5b1fe271";'
              'z_c0="2|1:0|10:1539235762|4:z_c0|92:Mi4xVGtJSUFBQUFBQUFBZ0NlX3UzbFlEaVlBQUFCZ0FsVk5zaTJzWEFETkxVdzRvZ2J3ZkRPd2M4dWt6RUZMd0RDTXlB|101fa019b4c16744491c6d93a0d281ffeb3b381372397363113211c9f376b775"',
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
r = requests.get('https://www.zhihu.com', headers=headers)
print(r.text)
