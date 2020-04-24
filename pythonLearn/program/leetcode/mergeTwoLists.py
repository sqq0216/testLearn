#合并两个有序链表
'''
链表ListNode 为自定义类
一个对象时一个节点，且该节点链接下一个节点
注意事项：判断为空、判断过程中其中一个为空时直接链接另一个
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        tmp = ListNode(0)
        res = tmp
        while l1 is not None and l2 is not None:
            # print(l1.val)
            if l1.val<=l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next
        if l1 is None:
            tmp.next = l2
        elif l2 is None:
            tmp.next = l1
        return res.next

if __name__ == "__main__":
    node01 = ListNode(1)
    node02 = ListNode(2)
    node03 = ListNode(4)
    
    node11 = ListNode(1)
    node12 = ListNode(3)
    node13 = ListNode(4)
    
    node01.next = node02
    node02.next = node03
    node11.next = node12
    node12.next = node13

    sol = Solution()
    res = sol.mergeTwoLists(node01, node11)
    list=[]
    for i in range(0,6):
        list.append(res.val)
        res = res.next
    print(list)
    
