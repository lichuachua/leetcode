# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        arr = []
        while head:
            arr.append(head)
            head = head.next
        temp = result
        for i in range(len(arr) - 1, -1, -1):
            arr[i].next = None
            temp.next = arr[i]
            temp = temp.next
        return result.next
