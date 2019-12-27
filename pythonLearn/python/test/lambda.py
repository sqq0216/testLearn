# 匿名函数
# def is_odd(n):
#     return n % 2 == 1

# L = list(filter(is_odd, range(1, 20)))
# for i in L:
#     print(i)
# 将以上代码改造为匿名函数(lambda:不需要定义一个函数的时候)
L = list(filter(lambda x: x % 2 ==1, range(1,20)))
for i in L:
    print(i)