# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
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

        # 比较
        while res:
            if res.val != head.val:
                return False
            res = res.next
            head = head.next

        return True


"""

Solution:反转链表
找到链表中点，反转后半部分，遍历前半部分和后半部分，看是否一致。
注意：
不能直接全部反转后进行比较，因为我们只能在原链表上进行反转，反转后找不到原链表
"""
