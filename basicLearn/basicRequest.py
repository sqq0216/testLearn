import requests

# 将一些复用较高的代码方法封装到一个类中
class BaseRequest(object):
    # 构造器
    def __init__(self):
        self.base_url = "http://39.107.96.138:3000/api/v1"
    def request(self,url,method=None,data=None):
        if method == "Get":
            return requests.get(self.base_url+url,params=data)
        elif method == "Post":
            return requests.post(self.base_url+url,json=data)
        