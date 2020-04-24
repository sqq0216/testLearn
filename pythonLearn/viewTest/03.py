n,m=map(int,input().split())
li = []
for i in range(n):
    num = input()
    lis = []
    for j in str(num):
        lis.append(j)
    li.append(lis)
print(li)
for k in range(n):
    for s in range(len(li[k])):
        if int(li[k][s]) == 0:
            print(0,end=' ')
        else:
            if 0 in [li[k][s+1],li[k+1][s]]:
                print(1,end=' ')
            
    print(' ')


