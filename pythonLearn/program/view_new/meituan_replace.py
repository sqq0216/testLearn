# 重写replace方法

def replace(s,a,b):
    
    s_res = list(s)
    i = 0
    while i <= len(s)-len(a):
        if s_res[i] == a[0]:
            if s[i:i+len(a)] == a:
                s_res[i:i+len(a)] = list(b)
                i += len(a)
        i += 1
    res = ''.join(s_res)
        
    return res

s ='abcdabcd' 
a = 'bc'
b ='BC'
print(replace(s,a,b))