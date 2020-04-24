# 快速排序 时间复杂度为O（n）或O（n^2）平均时间复杂度为O(nlogn)   空间复杂度O（logn）/O(n)
import random
def qsort(l):
    if len(l) < 2:
        return l
    else:
        base = l[0]
        left = [ele for ele in l[1:] if ele < base]
        
        right = [ele for ele in l[1:] if ele > base]
        
        return qsort(left) + [base] + qsort(right)
# 冒泡排序 时间复杂度为O（n^2）最佳为O（n）
def boublesort(l):
    n = len(l)
    for i in range(n):
        for j in range(0, n-i-1): 
            if l[j] > l[j+1] :
                l[j], l[j+1] = l[j+1], l[j]

        
if __name__ == "__main__":
    test1 = []
    num = random.randint(0,10)
    for i in range(num):
        test1.append(random.randint(0,5))
    print(test1, num)
    print(qsort(test1))
    # l=[8,4,6,7,3]
    # random.shuffle(l)
    # boublesort(l)
    # for i in range(len(l)):
    #     print(l[i])
