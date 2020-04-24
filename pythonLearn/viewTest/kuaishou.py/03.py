n,k,m = 4, 2, 2
# li = []
# for i in range(1,n+1):
#     li.append(i)
# print(li)
li = [1,2,3,4]
cur = k
while len(li)!=1:
    print(li.pop(li.index(cur)+m-1-len(li)))
    cur = li[li.index(cur)+m-1-len(li)]
print(li[0])

import sys
line = sys.stdin.readline().strip()
values = list(map(int, line.split()))