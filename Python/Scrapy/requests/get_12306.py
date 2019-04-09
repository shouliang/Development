import requests
from requests.packages import urllib3

# response = requests.get('https://www.12306.cn')

urllib3.disable_warnings()
response = requests.get('https://www.12306.cn', verify=False)

print(response.status_code)