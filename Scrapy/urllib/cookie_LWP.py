import http.cookiejar, urllib.request

# 将cookie保存成libwww-perl(LWP)的格式
filename = 'cookies_LWP.txt'
cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')

cookie.save(ignore_discard=True, ignore_expires=True)
