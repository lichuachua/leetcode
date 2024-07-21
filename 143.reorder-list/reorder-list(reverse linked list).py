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
        # 找中点
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 反转后半部分
        tmp, res = None, None
        while slow:
            tmp = slow.next
            slow.next = res
            res = slow
            slow = tmp
        # 组装
        first, second = head, res
        while second.next:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
        return first


"""
Solution:反转链表
通过观察可以发现，链表可以分成两部分，前半部分按序遍历，后半部分需要逆序遍历
反转链表类似题206，更相似0234. 回文链表
两部分链表进行组装，
"""
