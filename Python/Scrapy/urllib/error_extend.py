from urllib import request, error

# HTTPError是URLError的子类，先捕获子类，再去捕获父类的错误
try:
	response = request.urlopen('https://cuiqingcai.com/index.htm')
except error.HTTPError as e:
	print(e.reason)
	print(e.code)
	print(e.headers)
except error.URLError as e:
	print(e.reason)
else:
	print('Request Successfully')