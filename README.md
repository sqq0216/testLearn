# python测试开发知识积累
项目中包含以下几部分内容，部分详细介绍在对应的单独模块的readme文件中
## 分层的自动化测试
1. Unit（数据处理层）---单元/模块测试（code review/unittest）
2. servic（业务逻辑层）---集成/web接口测试(request库+unittest)
2. UI（UI界面层）---ui自动化测试/JS自动化测试（selenium库+unittest库）
## 自动化测试分类
1. unittest单元测试 ——unittest库/pytest单元测试库（比unittest更适用于做UI自动化，因为其可通过conftest.py文件配置浏览器的启动关闭，可以运行失败截图，运行失败重跑）
2. web UI 自动化测试——unittest库 + selenium
3. HTTP接口自动化测试——unittest库 + requests库
4. 移动自动化测试——unittest + appnium
## web开发--Django框架
## 库、框架、工具
1. 库(selenium、request等)
2. 自动化测试框架（unitest、pytest、robot framework（关键字驱动测试框架））
3. 自动化测试工具（UFT(QTP)、Katalon）
  - postman jmeter fidller badboy
4. 自动化测试框架的搭建
- WebUI:
  + 设计模式：基于关键字驱动，结合数据驱动的设计模式进行构建。
  + 对selenium中常用的方法比如元素定位、操作等进行二次封装形成类对象，作为工具类使用，使用unittest/pytest编写测试用例，也可以通过yaml/ddt/excel的形式做数据驱动的文件读写，结合关键字调用实现一系列的流程，最后将断言结果写入文件中，作为测试结果的判断标准。
- 接口测试
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
- 测试数据和测试脚本分开，即测试数据单独存放到一个文件中，通过读取数据执行测试用例，不同的数据测试不同的功能，测试时只需修改数据文件即可
4. 关键字驱动测试：以填表格的方式进行测试，避免操作代码
- 将同样的业务逻辑编写成类或者函数作为关键字供测试脚本调用，（被操作对象（Item）、操作（operation）和值（value））通过组合测试数据和关键字完成测试用例的编写，最终达到一个由数据和关键字驱动整个测试的效果
## jenkins
### 简介
基于Java开发的一种持续集成工具，用于监控程序重复的工作，可在tomcat中运行
### 安装
1. 安装Java环境
2. 下载tomcat并解压
2. 下载Jenkins，安装路径选择tomcat/webapps
### Q&A
1. 安装完成后，启动tomcat的start.bat失败
  - 在setclasspath文件中配置JAVA_HOME和JRE_HOME即可
