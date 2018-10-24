from selenium import webdriver
from selenium.webdriver import ActionChains

# 动作链
browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_id('draggable')
target = browser.find_element_by_id('droppable')
actions = ActionChains(browser)

# 实现拖拽
actions.drag_and_drop(source, target)
actions.perform()
