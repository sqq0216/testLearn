#-*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        l = []
        while listNode:
            l.append(listNode.val)
            listNode = listNode.next
        print(l)
        print(l[-1::-1])
        res = l[-1::-1]
        return res

if __name__ == "__main__":
    node01 = ListNode(1)
    node02 = ListNode(2)
    node03 = ListNode(4)
    
    node01.next = node02
    node02.next = node03
    

    sol = Solution()
    res = sol.printListFromTailToHead(node01)
    
    print(res)
    