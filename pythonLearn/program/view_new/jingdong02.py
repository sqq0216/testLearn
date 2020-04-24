# n, m = map(int,input().split())
# li = []
# qli = []
# for i in input().split():
#     li.append(int(i))
# q = int(input())
# for k in range(q):
#     qli.append(int(input()))
# li.sort()
m = 2
li = [1,2,3,4,5]
qli = [3,5]

for i in qli:
    res = 0
    start = i-1
    num = 1
    while start -2  >= 0:
        for k in li[start:start-2:-1]:
            print("k*num",k*num)
            res += k*num
        start -= m

    