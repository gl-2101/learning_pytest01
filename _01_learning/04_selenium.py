'''
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.cnblogs.com/jessonluo/p/4717140.html")

'''

from selenium import webdriver

import time

#如果无法找到驱动，加上os.environ['webdriver.firefox/chrome/IE.dirver'] = '浏览器驱动原始路径'

#driver = webdriver.Firefox(executable_path='d:\\geckodriver')  #浏览器驱动存放的位置

driver = webdriver.Chrome(executable_path='c:\\chromedriver')


driver.get('https://www.baidu.com')  #打开百度搜索页面

driver.find_element_by_id('kw').clear() #清除输入框内容

driver.find_element_by_id('kw').send_keys(u'测试')

driver.find_element_by_id('su').click()

time.sleep(3)

driver.quit()
