import api02
import unittest

class TestApi(unittest.TestCase):
    #测试用例：发布话题
    def test_01postTopic(self):
        #调用用例方法
        r=create_new_topic()

        #添加断言
        self.assertEqual(r.status_code,200,"状态码应该未200")
