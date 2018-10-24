import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)

try:
    browser.get('https://login.taobao.com/member/login.jhtml')
    input_username = wait.until(EC.presence_of_element_located((By.ID, 'TPL_username_1')))
    input_password = wait.until(EC.presence_of_element_located((By.ID, 'TPL_password_1')))
    submit = wait.until(EC.element_to_be_clickable((By.ID, 'J_SubmitStatic')))
    input_username.clear()
    input_username.send_keys('shouliang0816111')
    input_password.clear()
    time.sleep(3)
    input_password.send_keys('tbliang520')
    time.sleep(3)
    submit.click()
except TimeoutException:
    print('time out')

browser.execute_script('window.open()')
print(browser.window_handles)
# browser.switch_to.window(browser.window_handles[1])
# browser.get('https://s.taobao.se')
# time.sleep(1)
#
# # 切换选项卡
# browser.switch_to.window(browser.window_handles[0])
# browser.get('https://python.org')
