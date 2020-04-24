n = int(input())
lis = []
line = 0
while n > 0:
    x,y = map(int,input().split())
    lis.append(x)
    line += x
    n -= 1
res = 0
lin = line // len(lis)
for i in lis:
    res += abs(i-lin) 
print(res)
# res = max(lis) * len(lis)
# for i in range(max(lis)+1):
#     sum = 0
#     for j in lis:
#         sum += abs(j-i)
#     if sum < res:
#         res = sum
# print(res)