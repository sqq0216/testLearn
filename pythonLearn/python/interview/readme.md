# python 面试常见问题
## python常用库
1. request:接口自动化（get post put等）
2. selenium：web 的ui自动化（定位web元素并对其进行操作）
3. appnium： app的ui自动化
4. re:正则表达式
## python数据类型
1. 整型--int
2. 布尔型--bool
3. 字符串--str               ''/""/
4. 列表--list（有序，可改变） []
5. 元组--tuple（有序，不可变）()
6. 字典--dict（无序，可改变） {}
7. 集合--set(无序，不重复)    set([])  {}
## python2 和python3的区别
1. 安静来看python2和python3的最大区别就是编码问题了。python2中使用ascii编码，python3中使用utf-8编码
2. 异常
3. 一些方法如print
## python如何操作excel表
第3方库xlwr和xlrd，其中xlwr是对Excel进行写，xlrd是对Excel进行读。
## *arg和*kwarg的区别
简单的来说就是可以是我们的函数引入多个实参
- *arg返回的是字典
- *kwarg返回的是元祖
## python连接数据库
- python2通过MYSQL-python；
- python3通过pyMysql
## 自动化测试通过什么保存数据
通过yaml或者是ini
## 提高运行效率
1. 使用生成器，因为可以节约大量内存
2. 循环代码优化，避免过多重复代码的执行
3. 核心模块用Cython PyPy等，提高效率
4. 多进程、多线程、协程
5. 多个if elif条件判断，可以把最有可能先发生的条件放到前面写，这样可以减少程序判断的次数，提高效率

