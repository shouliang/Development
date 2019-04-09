import urllib.parse
import urllib.request

# post中的data数据为bytes字节流类型
# 通过urllib.parse.urlencode()方法将参数字典转化为字符串
data = bytes(urllib.parse.urlencode({'word':'hello'}), encoding='utf8')
response = urllib.request.urlopen('http://httpbin.org/post',data = data)
print(response.read())

