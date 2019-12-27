x = 1534236469
flag = -1 if x<0 else 1
x_new = x*flag
Length = 0
x_judge=x_new
while x_judge != 0:
    Length += 1
    x_judge = x_judge // 10
#print(x_new,x_judge)
#if x_new > 0 and x_new < (2**31)-1:
i = Length-1
x_res = 0
while i >=0:
    x_res += x_new % 10 * (10**i)
    if x_res < (-2**31) or x_res > (2**31-1):
        x_res = 0
        break
    x_new = x_new // 10
    i -= 1
print(x_res*flag)

