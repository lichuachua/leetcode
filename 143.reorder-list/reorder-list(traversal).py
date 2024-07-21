# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return
        tmp = head
        listArray = []
        while tmp is not None:
            listArray.append(tmp)
            tmp = tmp.next
        left, right = 0, len(listArray) - 1
        while left < right:
            listArray[left].next = listArray[right]
            left += 1
            listArray[right].next = listArray[left]
            right -= 1
        listArray[left].next = None


"""
Solution:遍历+双指针
链表不能通过下标访问，可以遍历将其存在数组中
之后按照下标进行重组
"""
