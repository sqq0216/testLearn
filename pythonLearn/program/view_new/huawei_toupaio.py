# li = list(map(str,input().split(',')))
li = ['Tom', 'Lily', 'Tom', 'Lucy', 'Lucy', 'Jack']
di = {}
for i in li:
    if i not in di:
        di[i]=1
    else:
        di[i] += 1

num = 0
res = ''
for j in di:
    if di[j]>num:
        num = di[j]
        res = j
    elif di[j] == num:
        if j < res:
            res = j
        
print(res)    


