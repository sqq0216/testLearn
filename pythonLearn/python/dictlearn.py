#字典相关函数

#字典值最大的键值对列表
def max_pairs(dic):
    if len(dic) == 0:
        return dic
    else:
        #map() 生成的是迭代器不是list， 你可以在map前加上list，即list(map())
        #return list(map(lambda v: v[1], dic.items()))
        max_val = max(map(lambda v: v[1], dic.items()))
        return [item for item in dic.items() if item[1] == max_val]

#字典值最小的键值对列表
def min_pairs(dic):
    if len(dic) == 0:
        return dic
    else:
        min_values = min(map(lambda v: v[1], dic.items()))
        return [item for item in dic.items() if item[1] == min_values]

#求字典前n个的最大值(返回字典d前n个最大值对应的键)
from heapq import nlargest, nsmallest

def topn_dict(d, n):
    #return nsmallest(n, d, key=lambda k: d[k])
    return nlargest(n, d, key=lambda k: d[k])

#合并两个字典
def merge_dict2(dic1, dic2):
    #return {**dic1, **dic2}  # python3.5后支持的一行代码实现合并字典
    dic1_list = list(dic1.items())
    dic2_list = dic2.items()
    # print(dic1_list)  : dict_items([('a', 1), ('b', 2), ('c', 3)])
    # print(type(dic1_list)) :  <class 'dict_items'>
    for item in dic2_list:
        dic1_list.append(item)
    return dic1_list

#集合
#互为变位词
from collections import Counter
# 检查两个字符串是否 相同字母异序词，简称：互为变位词
def anagram(str1, str2):
    print(Counter(str1), Counter(str2))

    return Counter(str1) == Counter(str2)


if __name__ == "__main__":
    dic1 = {'a':1, 'b':2, 'c':3}
    dic2 = {'d':4, 'e':5, 'f':6}
    # print(min_pairs({'a': -10, 'b': 5, 'c': 3, 'd': 5}))
    #print(topn_dict({'a': 10, 'b': 8, 'c': 9, 'd': 10}, 3))
    # print(merge_dict2(dic1,dic2))
    print(anagram('eleven+two', 'twelve+one'))  # True 这是一对神器的变位词
    print(anagram('eleven', 'twelve'))  # False

