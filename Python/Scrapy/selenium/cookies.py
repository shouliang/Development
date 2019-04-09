from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
# 获取cookies
print(browser.get_cookies())

browser.add_cookie({'name':'zhangsan', 'domain':'www.zhihu.com', 'value': 'germey'})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())