from selenium import webdriver
from time import sleep
from modulize import Log

driver = webdriver.Chrome()
driver.get("http://www.126.com")
sleep(3)
log = Log(driver)
log.login("sunqianqian_0216", "sqq610101046")
#log.logout()
driver.quit()

