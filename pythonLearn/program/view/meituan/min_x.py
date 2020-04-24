# 给一个n大小的列表l，一个目标数x,从列表取出几个数之后，最大减去最小的小于x,求最少取出几个数
# 待优化：有些情况减去最小值更优
n, x = map(int, input().split())
l = []
num = input()
for i in num.split():
    l.append(int(i))

res = 0
while max(l) - min(l) > x:
    l.remove(max(l))
    res += 1

print(res)





