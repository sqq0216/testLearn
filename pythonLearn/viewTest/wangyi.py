import sys
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     ans = 0
#     for i in range(n):
#         # 读取每一行
#         line = sys.stdin.readline().strip()
#         # 把每一行的数字分隔后转化成int列表
#         values = list(map(int, line.split()))
#         for v in values:
#             ans += v
#     print(ans)
n = int(input())
x = []
y = []
while n > 0:
    xi, yi,xj,yj = map(int,input().split())
    x.append(xi)
    x.append(xj)
    y.append(yi)
    y.append(yj)
    n -= 1
res = (max(x)-min(x)) * (max(y)-min(y))
print(res)

