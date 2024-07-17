# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 原地反转-头插法
        result = None
        tmp = None
        while head:
            tmp = head.next
            head.next = result
            result = head
            head = tmp
        return result


"""
Solution:原地反转-头插法
迭代的思想，新建链表，遍历一次链表，两两元素反转，每次在新的链表头部插入元素
"""
