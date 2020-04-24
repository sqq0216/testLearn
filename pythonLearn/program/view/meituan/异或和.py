
n= int(input())
l = []
l_row = input()
for i in l_row.split():
    l.append(int(i))


lis = []
for i in range(0,len(l)):
    for j in l[i+1:]:
        if l[i] != j:
            lis.append(0)
        else:
            lis.append(1)
res1 = lis.count(0)
res2 = lis.count(1)
if res2  % 2 == 0:
    print(0)
else:
    print(1)




