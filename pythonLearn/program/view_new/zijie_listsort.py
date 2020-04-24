# 对字典列表排序
li = [{'name':'zhang','age':3},{'name':'san','age':5},{'name':'li','age':1},{'name':'si','age':2},]
# li.sort(key=lambda li: li['age'])
# print(li)
b= sorted(li,key=lambda li: li['age'])
print(li,'\n',b)
