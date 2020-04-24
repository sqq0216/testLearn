#coding=utf-8
import sys

# line = sys.stdin.readline().strip()
# values = list(line.split())
# li = values[0]

li = '(3+)))((('
base = '()'
res = [0]
num1 = 0
left = li.count('(')
right = li.count(')')
for i in li:
    if i == base[0]:
        res.append(i)
    elif i == base[1] and res[-1] != 0:
        res.pop()
        num1 += 1
    elif res[-1] == 0:
        
        break
print(num1,left-num1,right-num1)


