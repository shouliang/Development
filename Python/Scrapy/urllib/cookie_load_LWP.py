import http.cookiejar, urllib.request

cookie = http.cookiejar.LWPCookieJar()
# 利用load()方法读取本地的Cookie文件
cookie.load('cookies_LWP.txt', ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')

print(response.read().decode('utf-8'))