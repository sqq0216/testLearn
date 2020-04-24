# tar = 'read'
# base = 'read[addr=0x17,mask=0xff,val=0x7],read_his[addr=0xff,mask=0xff,val=0x1],read[addr=0xf0,mask=0xff,val=0x80]'

# li = list(base.split('],'))
# for i in li:
#     print("+++",i)
#     if i[:len(tar)] == tar:
#         for j in range(len(i)):
#             if i[j] == "=":
#                 print(i[j+1:j+5])

# 5 2 3 1 0 0
# 1 20 2 3
# 2 30 3 4 5
# 3 50 4
# 4 60
# 5 80
# n1 = list(map(int,input().split(' ')))
# li = []
# di = {}
# for i in range(n1[0]):
#     inp = list(map(int,input().split(' ')))
#     di[i+1] = inp.pop(1)
#     li.append(inp)
# print(li,di)
li = [[1, 2, 3], [2, 3, 4, 5], [3, 4], [4], [5]]
di = {1: 20, 2: 30, 3: 50, 4: 60, 5: 80}
res = []
for l in li:
    num = 0
    for j in l:
        num += di[j]
    res.append(num)
print(max(res))

    

