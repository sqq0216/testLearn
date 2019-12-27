#冒泡排序
a = [1,6,4,2,67,32]
l = len(a)
for i in range(l):
   for j in range(l-1):
       if a[j] > a[j+1]:
           a[j],a[j+1] = a[j+1],a[j]
for i in range(l):
   print(a[i])

#用python内置函数
# a = [1,6,4,2,67,32]
# m = sorted(a)
# print(m)
# # 代码结果
# [1, 2, 4, 6, 32, 67]
# # 也可通过其他函数
# a.sort()