# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 新建节点-头插法
        result = None
        while head:
            result = ListNode(head.val, result)
            head = head.next
        return result


"""
Solution:原地反转-头插法
迭代的思想，新建链表，遍历一次链表，两两元素反转，每次在新的链表头部插入元素
和1不同的是，1是在原来的结点基础上链接起来的，而下面的代码是新建结点
"""
