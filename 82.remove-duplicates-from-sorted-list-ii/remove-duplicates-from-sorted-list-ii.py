# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        res = ListNode(0, head)
        tmp = res
        while tmp.next is not None and tmp.next.next is not None:
            if tmp.next.val == tmp.next.next.val:
                duplicatesNum = tmp.next.val
                while tmp.next is not None and tmp.next.val == duplicatesNum:
                    tmp.next = tmp.next.next
            else:
                tmp = tmp.next
        return res.next
