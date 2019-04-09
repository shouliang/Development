from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')

# 执行JavaScript脚本
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
browser.execute_script('alert("To Bottom")')
