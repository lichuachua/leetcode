# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 原地反转-头插法
        result = None
        tmp = None
        while head:
            tmp = head.next
            head.next = result
            result = head
            head = tmp
        return result

    def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        result = res
        jinwei = 0
        while l1 is not None and l2 is not None:
            s = l1.val + l2.val + jinwei
            l1, l2 = l1.next, l2.next
            if s > 9:
                res.next = ListNode(s - 10)
                jinwei = 1
            else:
                res.next = ListNode(s)
                jinwei = 0
            res = res.next
        while l1 is not None:
            s = l1.val + jinwei
            l1 = l1.next
            if s > 9:
                res.next = ListNode(s - 10)
                jinwei = 1
            else:
                res.next = ListNode(s)
                jinwei = 0
            res = res.next
        while l2 is not None:
            s = l2.val + jinwei
            l2 = l2.next
            if s > 9:
                res.next = ListNode(s - 10)
                jinwei = 1
            else:
                res.next = ListNode(s)
                jinwei = 0
            res = res.next
        if jinwei == 1:
            res.next = ListNode(1)
            res = res.next
        return result.next

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        res = self.addTwoNumbers2(l1, l2)
        return self.reverseList(res)


g = ListNode(4, None)
f = ListNode(6, g)
e = ListNode(5, f)

d = ListNode(3, None)
c = ListNode(4, d)
b = ListNode(2, c)
a = ListNode(7, b)

re = Solution()
result = re.addTwoNumbers(a, e)
while result is not None:
    print(result.val)
    result = result.next
