from urllib import request, error 

try:
	response = request.urlopen('https://cuiqingcai.com/index.htm')
except error.HTTPError as e:
	# print(e.reason, e.code, e.headers, seq='\n')
	print(e.reason)
	print(e.code)
	print(e.headers)