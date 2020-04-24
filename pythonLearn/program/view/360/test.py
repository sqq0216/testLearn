import re
n = int(input())
m = int(input())
res = 0
list1 = str(m).split('0')
num = 0
num1 = 0
base = 1
for i in list1:
    for j in i:
        num1 += base
        base +=1
    num += num1
print(num)
list2 = re.split('0|2',str(m))
print("list2:",list2)
num5 = 0
base5 = 1
for i5 in list2:
    for j5 in i5:
        num51 = 0
        num51 += base5
        base5 +=1
    num5 += num51
print(num5)
res = (num+num5)/2
print(res)