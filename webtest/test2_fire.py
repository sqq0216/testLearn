from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# keys类提供了键盘的代码（回车,ALT,F1等等）

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
#通过元素的name属性来定位一个文本输入框元素
elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()