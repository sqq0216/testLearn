# def turn(num:int,str:str):
#     dir = "WNESWNESWNESWNES"
#     res = 5
#     print(dir[res])
#     for i in str:
#         if i == "L":
#             res -= 1
#         else:
#             res += 1
#     print(res)
#     return dir[res]
# if __name__ == "__main__":
#     print(turn(3,"LRR"))
N=int(input("please input a number:"))
str=input("please input a string include L and N:")
if len(str)==N:
    current='N'  
    for i in str:
       d={'N': 0,'W':1,'S':2,'E':3}
       m=[['W','E'],['S','N'],['E','W'],['N','S']]
       j=d[current]
       if i=='L':
           a=0  
       else:
           a=1  
       current=m[j][a]
    print(current) 
else: 
    print("the str's length must equle N")
