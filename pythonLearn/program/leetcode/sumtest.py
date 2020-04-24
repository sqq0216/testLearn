#两数之和

sum = [2, 7, 3, 6]
target = 9
# for j in range(len(sum)):
#     print(j)
j = -1
res_list=[]
for i in range(0,len(sum)-1):
    #print(i)
    num2 = target - sum[i]
    if num2 in sum[i+1:4]:
        #print(sum[i+1:3])
        if sum.count(num2) == 1 and num2 == sum[i]: # count()用于计算列表中有几个查找元素
            continue
        else:
            j = sum.index(num2, i+1)
            res = [i,j]
            res_list.append(res)
            continue
if j>0:
    print(res_list)
else:
    print("there is no a number for the ",target)
