import requests

r = requests.get('http://httpbin.org/get')
print(r.text)
print(type(r.text))
print(r.json())
print(type(r.json()))

print('--------------------')
data = {
    'name': 'germey',
    'age': 22
}
r = requests.get('http://httpbin.org/get', params=data)
print(r.text)


