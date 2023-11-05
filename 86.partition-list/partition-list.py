# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # 双栈
        head1, head2 = ListNode(0, None), ListNode(0, None)
        res1, res2 = head1, head2
        while head is not None:
            if head.val < x:
                head1.next = head
                head1 = head1.next
            else:
                head2.next = head
                head2 = head2.next
            head = head.next
        head2.next = None
        head1.next = res2.next
        return res1.next

