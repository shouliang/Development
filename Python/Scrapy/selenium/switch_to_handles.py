import time
from selenium import webdriver

# 选项卡管理
browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to.window(browser.window_handles[1])
browser.get('https://www.taobao.com')
time.sleep(1)

# 切换选项卡
browser.switch_to.window(browser.window_handles[0])
browser.get('https://python.org')