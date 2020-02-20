# python测试开发知识积累
## 分层的自动化测试
1. Unit（数据处理层）---单元/模块测试（code review/unittest）
2. servic（业务逻辑层）---集成/web接口测试(request库+unittest)
2. UI（UI界面层）---ui自动化测试/JS自动化测试（selenium库+unittest库）

## unittest单元测试 ——unittest库
## web UI 自动化测试——unittest库 + selenium
## HTTP接口自动化测试——unittest库 + requests库
## 移动自动化测试——unittest + appnium

## web开发--Django
## 学习关键点：封装、PO、组织用例、框架设计、BDD\TDD(保证代码质量，功能)  
## 测试工具
postman jmeter fidller badboy
## 库、框架、工具
1. 库(selenium、request等)
2. 自动化测试框架（unitest、pytest、robot framework（关键字驱动测试框架））
3. 自动化测试工具（UFT(QTP)、Katalon）
## 自动化测试模型
1. 线性测试：单纯模拟用户完整的操作场景
2. 模块化与类库：把重复的操作封装成单独的公共模块，对其进行调用
  - 比如对登录登出功能进行模块化
    + 将用户名和密码作为参数传给方法使用，通过调用方法传入不同的参数进行测试
  - 数据参数化：将测试数据放入到数据文件中，对其进行读写，即读写文件内容放入到列表中，调用方法时将列表元素作为参数
    + txt文件
    + csv文件
    + xml文件
    + json文件
3. 数据驱动测试：解决执行诸多不同的参数的测试用例，使把测试数据参数化提供给数据驱动使用
4. 关键字驱动测试：以填表格的方式进行测试，避免操作代码
# 待学内容
python巩固  Java复习
数据库
Linux命令
覆盖  单元测试主要技术手段
