import unittest
# 定义一个测试类，继承unittest.Testcase
class TestStringMethods(unittest.TestCase):

    # 测试脚手架 test fixture
    def setUp(self):
        print("setup")

    def tearDown(self):
        print("tearDown")
    #在函数前加上@classmethon，则该函数变为类方法，该函数只能访问到类的数据属性，不能获取实例的数据属性
    @classmethod
    def setUpClass(cls):
        print("setUpClass")
    #在所有方法前执行
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    # 测试方法(方法名要以test开头，执行顺序按照方法名的数字、大写字母、小写字母)——测试用例
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO') 

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
    def test_add(self):
        self.assertEqual(1+1,2)

# 测试运行器（test runner）
if __name__ == '__main__':
    unittest.main(verbosity=2)