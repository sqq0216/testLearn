
li1 = "abbbaassa"
def strsol(li):
    cur = li[0]
    num = 1
    res = list(li)
    base = 0
    for i in range(1,len(li)):
        if li[i] == cur:
            num += 1
            if num >2 and li[i+1]!= cur:
                del res[i+1-num:i+1]
                cur = li[i]
                num = 1
                base += 1
        else:
            cur = li[i]
            num = 1 
    if base == 0:
        return res      
    return strsol(res)

a= strsol(li1)
print(''.join(a))
    
