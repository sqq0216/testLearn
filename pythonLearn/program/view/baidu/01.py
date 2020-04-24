n = int(input())
m = int(input())

for k in range(0,n):
    num = int()

list1 = [10, 20, 30, 40, 50]
list2 = [4, 5, 6, 7, 8]
res = 0
for i in range(0,m):
    res += max(list1)
    list1.remove(max(list1))
    cl = n-(i+1)
    for j in range(0,cl):
        list1[j] = list1[j] - list2[j]
print(res)


