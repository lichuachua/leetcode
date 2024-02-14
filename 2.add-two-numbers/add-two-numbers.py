# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
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
