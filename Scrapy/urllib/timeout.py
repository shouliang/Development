import urllib.request
import urllib.error
import socket

# timeout参数设置超时时间，单位为秒
# 如果一个页面长时间未响应，就可以跳过对它的抓取
response = urllib.request.urlopen('http://httpbin.org/get', timeout=1)
print(response.read())

try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
