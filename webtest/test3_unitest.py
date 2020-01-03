import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# unitest单元测试框架的使用

# 测试用例类继承testcase
class PythonOrgSearch(unittest.TestCase):

    #初始化方法，其它方法需要调用它
    def setUp(self):
        self.driver = webdriver.Chrome()#webdriver的下载位置可以在括号中指定，但安装到python下的话不必指定
    
    #测试方法：均要以test开头
    # 测试方法1
    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.taobao.com/")
        self.assertIn("淘宝", driver.title)
        elem = driver.find_element_by_id("q")
        elem.send_keys("棉服")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()