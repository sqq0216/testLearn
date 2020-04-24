# while True:
#     n = int(input())
#     list = ['0', '1']
#     res = 0
#     for i in range(1,n+1):
#         i_str = str(i)
#         for j in range(0,len(i_str)):
#             if i_str[j] not in list:
#                 break
#             else:
#                 if i_str[j] in list and j == len(i_str)-1:
#                     res += 1
#     print(res)

while 1:
    t = 0
    n = 1
    c=int(bin(n)[2:])
 
    number = int(input())
    while c <= number:
        t = t+1
        n = n+1
        c=int(bin(n)[2:])
        print("c is ", c)
        print(bin(n))
    print(t)