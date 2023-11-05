# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBookList(self, head: Optional[ListNode]) -> List[int]:
        res = []
        while head is not None :
            res = [head.val] + res
            head = head.next
        return res