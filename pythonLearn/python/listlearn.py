# 打印99乘法表
def ninelist():
    for i in range(1, 10):
        for j in range(1, i+1):
            print('{0}*{1}={2}'.format(j,i,j*i),end="\t")
        print()

#嵌套数组展开
from collections.abc import *

def flatten(input_arr, output_arr=None):
    if output_arr is None:
        output_arr = []
    for ele in input_arr:
        if isinstance(ele, Iterable): # 判断ele是否可迭代
            flatten(ele, output_arr)  # 尾数递归
        else:
            output_arr.append(ele)    # 产生结果
    return output_arr

#将list等分为子组
from math import ceil

def divide(lst, size:int):
    lstDiv = []
    #ceil():朝正无穷大方向取整
    for i in range(0, ceil(len(lst)/size)):
        lstDiv.append(lst[i*size:(i+1)*size])
    return lstDiv
    #return [lst[i * size:(i+1)*size] for i in range(0, ceil(len(lst) / size))]

#生成斐波那契序列的前n项
def fibonacci(n:int):
    fib = [1,1]
    if n == 1:
        return [1]
    elif n == 2:
        return fib
    else:
        while len(fib)<n:
            fib.append(fib[len(fib)-1]+fib[len(fib)-2])
        return fib

#过滤空值
def filter_false(lst):
    return list(filter(bool, lst))

#返回列表空元素
def head(lst):
    return lst[0] if len(lst) > 0 else None

#返回列表尾元素
def tail(lst):
    return lst[-1] if len(lst) > 0 else None

#对象转换为可迭代类型
from collections.abc import Iterable

def cast_iterable(val):
    return val if isinstance(val, Iterable) else [val]

#求最长列表
#参数前面加上* 号 ，意味着参数的个数不止一个，另外带一个星号（*）参数的函数传入的参数存储为一个元组（tuple），带两个（*）号则是表示字典（dict）
def max_length(*lst):
    #print(*lst)
    return max(*lst, key=lambda v: len(v), *lst)

#出现最多的元素
def max_frequency(lst):
    num = []
    for i in lst:
        num.append(lst.count(i))
    for j in lst:
        if lst.count(j) == max(num):
            return j
            break
    #return max(lst, default='列表为空', key=lambda v: lst.count(v))

#求多个列表的最大值和最小值
def max_num(*lst):
    return max(max(*lst, key=lambda v: max(v)))
    #return min(min(*lst, key=lambda v: min(v)))

#检查是否有重复元素
def has_duplicates(lst):
    #print(set(lst))
    for i in lst:
        if lst.count(i) > 1:
            return True
    return False 
    # return len(lst) == len(set(lst))

#求列表中所有重复元素
from collections import Counter

def find_all_duplicates(lst):
    # res = []
    # for i in lst:
    #     if lst.count(i) > 1:
    #         res.append(i)
    # return list(set(res))
    #counter():计算所有元素的个数，并返回一个字典
    c = Counter(lst) 
    print(c)
    return list(filter(lambda k: c[k] > 1, c))

#列表反转
def reverse(lst):
    return lst[::-1]

#浮点数等差数列
def rang(start, stop, n):
    #小数点后两位（有0 自动忽略）
    start,stop,n = float('%.2f' % start), float('%.2f' % stop),int('%.d' % n)
    #print(start, stop, n)
    step = (stop-start)/n
    lst = [start]
    while n > 0:
        start,n = start+step,n-1
        #round() 方法返回浮点数x的四舍五入值。
        lst.append(round((start), 3))
    return lst

if __name__ == "__main__":

    lst = [1, 3, 3, 2, 1, 1, 2]
    x = [1, 1, 2, 2, 3, 2, 3, 4, 5, 6]
    y = [1,2,3]
    #ninelist()
    #print(flatten([0,[1,2,3],[4,5,6]] ))
    #print(divide([1,2,3,4,5], 3))
    #print(fibonacci(5))
    #print(filter_false([None, 0, False, '', [], 'ok', [1, 2]]))
    #print(max_length([1, 2, 3], [4, 5, 6, 7], [8]))
    #print(max_frequency(lst))
    # print(max_num([1, 2, 3], [6, 7, 8], [4, 5]))
    # print(has_duplicates(x))
    # print(find_all_duplicates([1, 2, 2, 3, 3, 3]))
    print(rang(1,8,11))

