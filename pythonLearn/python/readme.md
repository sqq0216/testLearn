# 面向对象编程
1. 类的封装（将数据处理在类内部实现），继承，多态（继承之后可以继承方法也可以覆盖方法有自己的特色，即多态）
2. 使用__slots__，定义一个特殊的__slots__变量，来限制该class实例能添加的属性，对子类不起作用
3. property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查

# 面向对象高级编程

# 网络编程
1. python对字符串的修饰符，表明了特定的意义：常见就是如下几种：
1：r 这表示该字符串不进行转义，比如加在路径前：r"D:\data"，如果没有r你要写作:"D:\\data"
2：b 这表示该字串为字节串 bytes类型，
3：u 这表示该字符串采用utf-8编码 
2. TCP编程
- 客户端：
    - 创建socket
    - connect连接
    - send发送数据
    - recv接受数据
    - close关闭
- 服务端：
    - 创建socket
    - .bind绑定端口
    - listen监听
    - accept接收socket请求
    - resv send 传输数据
    - close关闭
3. UDP编程(不需要建立连接)
- 客户端：
    - 创建socket
    - sendto发送数据
    - recv接受数据
    - close关闭
- 服务端：
    - 创建socket
    - .bind绑定端口
    - resvfrom sendto 传输数据
    - close关闭
# WEB开发
1. http协议（get post put 等请求）
2. WSGI接口：通过函数相应HTTP请求（即编写符合WSGI标准的HTTP处理函数）
3. web 框架
4. 模板 
# 访问数据库
1. sqlite ：轻量级的关系型数据库，python内置，使用同jdbc相似
2. mysql :需要安装驱动，操作与jdbc类似
3. SQLAlchemy：python中最有名的ORM（Object-Relational Mapping）框架，把关系数据库的表结构映射到对象上

