# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        tmp = head
        while tmp.next is not None:
            if tmp.val == tmp.next.val:
                tmp.next = tmp.next.next
            else:
                tmp = tmp.next
        return head


"""
Solution:双指针遍历
两个指针指向当前元素和下一个元素，如果相等则跳过当前元素
"""
