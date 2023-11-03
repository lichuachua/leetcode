# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        pre = ListNode(0,head)
        res = pre
        while pre.next is not None :
            if pre.next.val == val :
                pre.next=pre.next.next
            else :
                pre = pre.next
        return res.next