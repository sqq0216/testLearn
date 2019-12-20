# selenium webdriver 
# selenium ide 录制回放
# 学习关键点：封装、PO、组织用例、框架设计、BDD\TDD(保证代码质量，功能)
from selenium import webdriver

#打开浏览器
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()
