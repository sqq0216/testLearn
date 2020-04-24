# m = int(input())
# li = []
# for i in range(m):
#     licur = []
#     for j in range(6):
#         l,w = map(int,input().split(' '))
#         licur.append(l)
#         licur.append(w)
#     li.append(licur)

li = [[1345, 2584, 2584, 683, 2584, 1345, 683, 1345, 683, 1345, 2584, 683], [1234, 4567, 1234, 4567, 4567, 4321, 4322, 4567, 4321, 1234, 4321, 1234]]

res = []
for l in li:
    resl = []
    for n in range(len(l)):
        if l.count(l[n]) % 2 != 0 and n <= len(l)-1:
            res.append('IMPOSSIBLE \n') 
            break
        elif n == len(l)-1 and l.count(l[n]) % 2 == 0:
            res.append('POSSIBLE \n')
            
        
    

print(''.join(res))

