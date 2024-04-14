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