from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input_first = browser.find_element_by_id('q')
input_second = browser.find_element_by_css_selector('#q')
input_third = browser.find_element_by_xpath('//*[@id="q"]')
print(input_first, input_second, input_third)

# find_element()是通用函数版本，第一参数是查找方式，第二个参数是值
print('------ find_element ------')
input_also_first = browser.find_element(By.ID, 'q')
print(input_also_first)

# find_elements 查找多个节点s
print('------ find_elements ------')
lis = browser.find_elements_by_css_selector('.service-bd li')
print(lis)

