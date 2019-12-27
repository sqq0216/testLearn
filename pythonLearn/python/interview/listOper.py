# 首先转换成集合
a = [1,3,3,4,4,5,5,6]
print(type(a))
m = set(a)
print(m)
print(type(m))
# 在从集合转换成列表
x  = [i for i in m]
print(x)
print(type(x))