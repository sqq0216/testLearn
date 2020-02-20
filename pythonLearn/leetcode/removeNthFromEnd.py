'''
删掉链表中指定的一个节点

注意事项：若链表只有一个节点，操作后将为空
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next is None:
            return None
        list = []
        while head is not None:
            list.append(head.val)
            head = head.next
        list.pop(-n)
        # print(list)
        res = ListNode(list[0])
        tmp = res
        for i in range(1,len(list)):
            tmp.next = ListNode(list[i])
            tmp = tmp.next
            # print(tmp.val)
        return res 

        """
        思路：
            计算链表元素的数量，减去n值得到要删除的节点的前一个节点的索引值，
        """
    def removeNthFromEnd2(self, head:ListNode, n: int) -> ListNode:
        if head.next is None:
            return None
        num = 0
        tmp = head
        res = tmp
        while head is not None:
            head = head.next
            num += 1
        newNum = num - n
        if newNum == 0:
            return res.next
        for j in range(0, newNum-1):
            tmp = tmp.next
        tmp.next = tmp.next.next
        return res



if __name__ == "__main__":
    node1=ListNode(1)
    node2=ListNode(2)
    node3=ListNode(3)
    node4=ListNode(4)
    node5=ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    sol = Solution()
    result = sol.removeNthFromEnd2(node1,1)
    list=[]
    while result is not None:
        list.append(result.val)
        result = result.next
    print(list)

