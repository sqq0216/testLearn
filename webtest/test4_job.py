from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
# unitest 与 selenium配合使用完成job查找并打印
class jobfind(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_find(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get("https://www.51job.com/")
        ele = driver.find_element_by_id("kwdselectid")
        ele.send_keys("python")
        ele.send_keys(Keys.RETURN)
        ele = driver.find_element_by_id("work_position_input")
        ele.click()
        #通过css表达式原则所有被选中的城市将其清空
        eles = driver.find_elements_by_css_selector("#work_position_click_center_right_list_000000 em[class=on]")

        for ele in eles:
            ele.click()
        driver.find_element_by_id("work_position_click_center_right_list_category_000000_010000").click()
        
        driver.find_element_by_id("work_position_click_bottom_save").click()
        time.sleep(10)
        #driver.find_element_by_css_selector('.ush  button').click()
        time.sleep(5)
        jobs = driver.find_elements_by_css_selector("#resultList div[class = el]")
        for job in jobs:
            fields = job.find_elements_by_tag_name("span")
            fieldString = [field.text for field in fields]
            print(" | ".join(fieldString))
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
