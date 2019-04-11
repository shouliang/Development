import http.cookiejar, urllib.request

# 将cookies保存成Mozilla型浏览器的Cookie格式
filename = 'cookies_Mozilla.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')

cookie.save(ignore_discard=True, ignore_expires=True)