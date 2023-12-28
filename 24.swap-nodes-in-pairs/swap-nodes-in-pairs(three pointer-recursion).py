# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 使用三个指针
        if head is None or head.next is None:
            return head
        slow, fast = head, head.next
        slow.next, fast.next = self.swapPairs(fast.next), slow
        return fast
