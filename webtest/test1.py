# selenium webdriver 
# selenium ide 录制回放

from selenium import webdriver

#打开浏览器
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
# 设置浏览器窗口大小
driver.maximize_window()
driver.set_window_size(480,800)  
