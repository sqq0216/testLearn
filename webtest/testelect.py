from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
#from openpyxl import workbook
import xlwt

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://www.51job.com/")
ele = driver.find_element_by_id("kwdselectid")
ele.send_keys("测试开发工程师")
ele.send_keys(Keys.RETURN)
ele = driver.find_element_by_id("work_position_input")
ele.click()
#通过css表达式原则所有被选中的城市将其清空
eles = driver.find_elements_by_css_selector("#work_position_click_center_right_list_000000 em[class=on]")

for ele in eles:
    ele.click()
driver.find_element_by_id("work_position_click_center_right_list_category_000000_010000").click()

ele = driver.find_element_by_id("work_position_click_bottom_save")
ele.click()
        
#time.sleep(10)
# ele = driver.find_element_by_css_selector('.ush  button')
#ele.click()
#time.sleep(5)
title = driver.find_element_by_css_selector('.dw_table .title ')
titlenames = title.find_elements_by_tag_name('span')
jobs = driver.find_elements_by_css_selector("#resultList div[class = el]")

#创建一个excel
book = xlwt.Workbook()
# 增加一个sheet
sh = book.add_sheet('统计')
# 写入内容
coll = 0
for name in titlenames:
    fieldTitle = [name.text]
    print('titlename', end=' ')
    sh.write(0,coll,fieldTitle)
    coll += 1

row = 1
for job in jobs:
    fields = job.find_elements_by_tag_name("span")
    col = 0
    for field in fields:
        fieldString = [field.text]
        #print(" | ".join(fieldString))#jion()函数，分割字符串（用|符号将string分割开）
        print(fieldString, end = ' ')
        sh.write(row, col,fieldString)
        col += 1
    print(' ')
    row += 1
#保存文件
book.save('d:\\TestProjects\\doc\\51job_测开.xls')

driver.quit()