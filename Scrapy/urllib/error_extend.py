from urllib import request, error

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