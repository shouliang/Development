import urllib.request

# 利用urllib.request的urlopen()函数打开一个网页
response = urllib.request.urlopen('https://www.python.org')

# urlopen的返回对象是<class 'http.client.HTTPResponse'>
# 它的read()方法可以得到返回的网页内容
# print(response.read().decode('utf-8'))

# status属性是返回结果的状态码，还是响应的头信息等
print(type(response))
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))