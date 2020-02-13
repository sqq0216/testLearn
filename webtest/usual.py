# selenium webdriver 
# selenium ide 录制回放

# driver常用操作
from selenium import webdriver
from time import sleep

#打开浏览器
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
# 设置浏览器窗口大小
driver.maximize_window()
#driver.set_window_size(480,800)  
try:
    text = driver.find_element_by_id('kw')
    #元素尺寸
    size = text.size
    print("size is :", size)
    #百度底部备案信息
    info = driver.find_element_by_id('cp').text
    print("底部信息：", info)
    #元素属性值（id name type）
    attrbut_id, attrbut_name, attrbut_type = text.get_attribute('id'), text.get_attribute('name'), text.get_attribute('type')
    print('属性',attrbut_id,attrbut_name, attrbut_type)
    #元素结果是否可见
    isdisplay = text.is_displayed()
    print(isdisplay)
    text.send_keys("selenium")
    sleep(3)
    text.submit()

except Exception as e:
    print(e)
finally:
    driver.quit()


