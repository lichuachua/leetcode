# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        # Create a dummy node to handle edge cases like reversing from the head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Move `prev` to the node before `left`
        for _ in range(left - 1):
            prev = prev.next

        # `start` is the first node of the sublist to be reversed
        start = prev.next
        then = start.next

        # Reverse the sublist from left to right
        for _ in range(right - left):
            start.next = then.next
            then.next = prev.next
            prev.next = then
            then = start.next

        return dummy.next


"""
Solution:原地反转-头插法
类似206的方法1
迭代的思想
1.Dummy Node: 创建一个虚拟节点 dummy，并将其 next 指向 head。这样在处理边界条件时，如从头开始反转链表时，操作会更简单。
2.寻找 left 前的节点：遍历链表 left - 1 次，找到 left 前的节点 prev。
3.开始反转子链表：
    start 是子链表的第一个节点。
    then 是 start 的下一个节点。
    通过循环，从 left 到 right，逐步将 then 插入到 prev 后面，逐步反转子链表。
4.返回新的头结点：由于 dummy.next 可能已经更新，所以返回 dummy.next。
"""
