from selenium import webdriver

# 声明浏览器对象
browser = webdriver.Chrome()
# 访问页面
browser.get('https://www.taobao.com')
# 打印出页面源代码
print(browser.page_source)
browser.close()