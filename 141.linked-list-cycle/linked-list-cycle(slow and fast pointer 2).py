# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

"""
Solution:快慢指针
类似142
快指针走两步，慢指针走一步，若存在环，迟早快慢指针相遇，若快指针到链表末尾，则无环

2的区别在于slow，fast的初始化 和 循环的条件
"""
