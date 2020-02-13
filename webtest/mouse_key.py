from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import unittest
from time import sleep
# keys类提供了键盘的代码（回车,ALT,F1等等）
# activechains 提供了鼠标的操作（定位，移动，点击等）
class MouseAndKeysTest(unittest.TestCase):
    # def __init__(self):
    #     self.driver = webdriver.Chrome()

    def setUp(self):
        print("开始测试")

    def tearDown(self):
        #self.driver.close()
        print("执行结束")

    # def test_keysSimple(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get("http://www.python.org")
    #     try:
    #         assert "Python" in self.driver.title
    #         elem = self.driver.find_element_by_name("q")
    #         elem.send_keys("pycon")
    #         elem.send_keys(Keys.RETURN)
    #         assert "No results found." not in self.driver.page_source
    #     except Exception as e:
    #         print(e)
    #     finally:
    #         self.driver.close()
    def test_mouse(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.cn")
        try:
            above = self.driver.find_element_by_link_text("设置")
            
            ActionChains(self.driver).move_to_element(above).perform()
            sleep(3)
        except Exception as e:
            print(e)
        finally:
            self.driver.close()
    def test_keys(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.cn")
        try:
            ele = 
        except expression as identifier:
            pass
        finally:
            pass


if __name__ == "__main__":
    unittest.main(verbosity=2)



    
