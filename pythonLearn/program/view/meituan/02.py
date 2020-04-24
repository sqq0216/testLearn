n = int(input())
m = [[0]*n for i in range(2)]
cou1 = input()
cou2 = input()
for i in cou1.split():
    i1 = 0
    print(i)
    m[0][i1] = str(i)
    i1 += 1
for j in cou2.split():
    j1 = 0
    m[1][j1] = str(i)
    j1 += 1
print(m[1][n-1])
print(m)
if m[1][n-1] == 'X':
    print(-1)