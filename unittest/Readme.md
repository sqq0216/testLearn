# 单元测试框架
用于编写和运行可重复的单元测试。主要用于进行白盒测试和回归测试，还适用于不同类型的自动化测试
## unittest（python自带的单元测试框架）
### 包含内容
1. 测试用例(unittest.testcase)
- 必须以test开头
2. 测试套件（test suit）（多个测试用例组合在一起）
- suit(组织当前模块中的测试用例，执行哪些以及执行顺序（顺序可以根据首字母也可以根据add顺序）)
  + suit = unitest.TestSuit()
  + suit.addTest(TestCalculator("test_..))
- discover（组织执行不同模块即不同文件中的测试用例）
  + 给定目录（test_dir）
  + suit = unittest.defaultTestLoader.discover(test_dir, pattern = 'test*.py')
  + 注：如果要执行指定目录的子目录下的测试用例，在子目录下添加__init__.py文件
3. 测试运行器（执行测试用例）
- TextTestRunner()
  + runner = unittest.TextTestRunner()
  + runner.run(suit)
- HTMLTestRunner()
  + runner = HTMLTestRunner(stream = fp, title, description)
  + runner.run (suit)
  + 在类或者方法后添加doc string注释，使报告更加易读
  + fp 的命名中加入时间进行版本区别
4. 测试脚手架（test fixture）
- setUp()/tearDown()---测试用例执行前后
- setUpClass()/tearDownClass()---测试类前后
- setUpModule()/tearDownModule()---模块前后
5. 测试报告
- htmltestrunner使用（github下载）
6. 跳过测试和预期失败（unitest提供了装饰器）(可以装饰方法或者类)
- unittest.skip("原因")
- unittest.skipIf()
- .skipUnless()
- .expectedFailure()
7. unittest扩展
- 数据驱动
  + 数据驱动(将测试数据写入文件，读取--数据文件读取)
  - 参数（parameterrized库，pip安装，在测试方法前注释（@parameterized.expand()））
  - ddt（pip安装，测试类需要通过@ddt装饰，其它同参数库使用（元组，字典，列表，数据文件）在方法前注释(@data()  @unpack)）
- 自动发送邮件
  + smtlib库
  + email模块
  + yagmail第三方库
- page object（对每一页元素定位操作的封装）
 + page object:自动化测试开发中应该遵循的一种设计模式，其设计思想是将元素定位与元素操作进行分层（当前端内容发生改变时，只需要维护page层的元素定位）
 + 将每个页面看作一个对象，完成元素定位和元素操作
 + poium测试库：基于selenium和appium的page object测试库，pip安装，提供了更加简单的元素定位方法
## pytest(pip安装)
### 与unittest单元测试框架的不同
1. 断言：unittest提供了不同的断言方法，pytest中没有专门的方法，直接使用python中的assert配合各种条件判断方法进行断言
2. fixture：
  - setup/teardown()
  - setup_function(function)
  - setup_module(module)
  - 支持使用测试类（同unittest）
    + setup/setup_method/setup_class
3. 参数化（同unittest用法相同，在方法前用@pytest.mark.parametrize()注释参数）
4. 运行测试：pytest命令加参数执行测试用例/或使用main方法
5. 测试报告：pytest支持生成多种测试报告
- JUnit XML文件（pytest ./test_dir --junit-xml=./report/log.xml）
- 生成在线测试报告（pytest ./test_dir --pastebin=all）
6. conftest.py(pytest特有的本地测试配置文件)
7. pytest扩展（通过pip安装）
- pytest-html
- pytest-rerunfailures
- pytest-parallel
## django自带的单元测试类（from django.test import TestCase）
