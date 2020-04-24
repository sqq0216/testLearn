# 游戏：n个格子，每个格子一个数，共有m分，没到一个格子减去格子中的分，m值不够结束
# 待完善：当m大于0时，不够减去格子数，仍然减去
# n, m = map(int, input().split())
# l = []
# num = input()
# for i in num.split():
#     l.append(int(i))
m = 15
n = 4
l = [2, 4, 6, 5]

j = 0
res = 0
while m > 0:
    if j == n:
        j = 0    
    if m < 0:
        break
    else:
        m -= l[j]
        j += 1
        res = res+1
if m >= min(l):
    res += 1
print(res)



