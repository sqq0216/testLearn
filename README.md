# python测试开发相关环境搭建
## web开发--Django
1. 下载安装  
在官网下载 https://www.djangoproject.com/download/ Django压缩包，解压之后在其目录下执行以下命令即可  
   - python setup.py install 
2. 验证   
在python交互环境中运行以下命令，看到相应版本说明安装成功  
   - import django
   - django.get_version()
3. 使用（可参考教程https://www.djangoproject.com/start/）
通过import导入即可使用
4. Q&A
   - 创建项目时运行“django-admin startproject autotest” ERRO:该命令不是内部命令或外部命令  
      - 解决：找到python目录下的django-admin.py文件然后将其复制到scripts目录下（该目录已经设置好环境变量）
## mysql & navicat
windows 官网下载后直接启动安装，然后使用navicat测试连接数据库
- 注意：mysql安装向导中有一个密码设置选择普通即可
## unitest
## request
## postman jmeter fidller badboy