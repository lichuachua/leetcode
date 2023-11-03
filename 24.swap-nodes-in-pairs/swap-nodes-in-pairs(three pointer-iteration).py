# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 使用三个指针
        res = ListNode(0,head)
        pre = res
        while head is not None and head.next is not None:
            slow,fast = head,head.next
            pre.next = fast
            slow.next = fast.next
            fast.next = slow
            pre,head = slow,slow.next
        return res.next

