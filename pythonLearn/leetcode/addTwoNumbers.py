#两数相加

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers0(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = 0
        num2 = 0
        i=0
        j=0
        res = ListNode(0)
        sum = res
        while l1 is not None:
            num1 += l1.val * 10**i
            l1 = l1.next
            i += 1
        while l2 is not None:
            num2 += l2.val * 10**j
            l2 = l2.next
            j += 1
        num = num1 + num2
        if num == 0:
            return 0
        while num != 0:
            res.next = ListNode(num % 10)
            num = num // 10
            res = res.next
        return sum.next
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2 
        elif l2 is None:
            return l1

        res = ListNode(0)
        tmp = res
        jinwei = 0
        while l1 is not None and l2 is not None:
            num = l1.val + l2.val + jinwei
            tmp.next = ListNode(num % 10)
            tmp = tmp.next
            jinwei = num // 10
            l1 = l1.next
            l2 = l2.next
        while l2 is not None:
            num = l2.val + jinwei
            tmp.next = ListNode(num % 10)
            tmp = tmp.next
            jinwei = num // 10
            l2= l2.next
        while l1 is not None:
            num = l1.val + jinwei
            tmp.next = ListNode(num % 10)
            tmp = tmp.next
            jinwei = num // 10
            l1= l1.next
        if jinwei != 0:
            tmp.next = ListNode(jinwei)
        return res.next
if __name__ == "__main__":
    list1 = [4,3]
    list2 = [6,4]
    l1 = ListNode(2)
    l2 = ListNode(5)
    ln1 =l1
    ln2 = l2
    for i in list1:
        l1.next = ListNode(i)
        l1 = l1.next
    for j in list2:
        l2.next = ListNode(j)
        l2 = l2.next
    sol = Solution()
    result = sol.addTwoNumbers(ln1, ln2)
    list=[]
    while result is not None:
        list.append(result.val)
        result = result.next
    print(list)

