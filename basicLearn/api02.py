import requests
from basicRequest import BaseRequest

token="96e1fd91-c68c-4f3c-8042-6a4b827df3da"

baseRequest = BaseRequest()
# get 主题首页
def homeTopic():
    params_data={
        "page":1,
        "tab":"ask",
        "limit":1,
        "mdrender":"true"
    }
    # r = requests.get(url=base_url+"/topics",params=params_data)
    r=baseRequest.request("/topics","Get",data=params_data)
    print(r)
    r_json=r.json()
    # print(r.status_code)
    # print(r_json["data"])
    r_suc=r.json()["success"]
    r_data=r.json()["data"]
    print(r_json)
    print("\n")
    print(type(r_json),type(r_data))
    assert 200==r.status_code
    assert True==r_suc
    assert 2==len(r_json)
    assert 1==len(r_data)

# post 创建主题
def creatTopic():
    body = {
        "accesstoken":token,
        "title":"qqqqqq",
        "tab":"ask",
        "content":"ggggggg"
    }
    # 如果参数写为data=body 则请求头为报表格式
    #r_creat=requests.post(url=base_url+"/topics",json=body) 
    r_creat=baseRequest.request("/topics","Post",data=body)#传参顺序不对的话会报错（AttributeError: 'NoneType' object has no attribute 'json'）
    print(r_creat.json())
    print(r_creat.status_code)
    print(r_creat.request.headers)
homeTopic()
creatTopic()