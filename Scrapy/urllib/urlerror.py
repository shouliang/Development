from urllib import request, error

# URLError来自urllib库中的error模块
# 它继承自OSError类，OSError是error异常模块的基类
# reason属性返回错误的原因
try:
    response = request.urlopen('https://cuiqingcai.com/index.htm')
except error.URLError as e:
    print(e.reason)
