# 测试的模块化（将常用的功能单独封装成公共模块）
# 参数化
from time import sleep
class Log:
    #初始化方法初始化driver
    def __init__(self, driver):
        self.driver = driver
    
    def login(self,username, password):
        # fr = self.driver.find_element_by_xpath("//iframe[starts-with(@id, 'x-URS-iframe')]")
        # self.driver.switch_to.frame(fr)
        
        # input = self.driver.find_element_by_xpath("//input[starts-with(@class, 'j-inputtext dlemail')]")
        # input.clear()
        # #input = self.driver.find_elements_by_tag_name("input")[0]
        # input.send_keys(username)
        self.driver.switch_to_default_content()
        self.driver.switch_to_frame(0)
        sleep(2)
        try:
            user = self.driver.find_element_by_xpath("//form[@id='login-form']/div[1]/div[1]/div[2]/input")
            user.clear()
            user.send_keys(username)
            # self.driver.find_element_by_name("email").click()
            # #self.driver.find_element_by_name("email").clear()
            # self.driver.find_element_by_name("email").send_keys(username)
            self.driver.find_element_by_name("password").clear()
            self.driver.find_element_by_name("password").send_keys(password)
            self.driver.find_element_by_id("dologin").click()
        except Exception as e:
            print(e)
        finally:
            return
    def logout(self):
        self.driver.find_element_by_link_text("退出").click()
    def test(self):
        #self.driver.find_element_by_link_text("企业邮箱").click()
        self.driver.find_element_by_id("switchAccountLogin").click()


        