import http.cookiejar, urllib.request

cookie = http.cookiejar.CookieJar()

# 通过HTTPCookieProcessor构造一个Handler
handler = urllib.request.HTTPCookieProcessor(cookie)

# 通过参数handler构造opener
opener = urllib.request.build_opener(handler)

response = opener.open('http://www.baidu.com')

# 遍历cookie
for item in cookie:
    print(item.name + "=" + item.value)
