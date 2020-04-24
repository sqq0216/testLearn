n = int(input())
m = int(input())
n1 = input()
m1 = input()
list1 = []
list2 = []
for i in n1.split():
    list1.append(int(i))
for j in m1.split():
    list2.append(int(j))

res = 0
for i in range(0,m):
    res += max(list1)
    list1.remove(max(list1))
    cl = n-(i+1)
    for j in range(0,cl):
        list1[j] = list1[j] - list2[j]
print(res)


