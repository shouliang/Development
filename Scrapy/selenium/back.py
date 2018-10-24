import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.get('https://www.taobao.com')
browser.get('https://www.python.org')

# 后退
browser.back()
time.sleep(1)

# 前进
browser.forward()
browser.close()