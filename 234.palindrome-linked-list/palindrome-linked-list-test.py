# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        a = []
        while head:
            a.append(head.val)
            head = head.next
        i, j = 0, len(a) - 1
        while i <= j:
            if a[i] != a[j]:
                return False
            i += 1
            j -= 1
        return True


e = ListNode(1, None)
d = ListNode(2, e)
c = ListNode(3, d)
b = ListNode(2, c)
a = ListNode(1, b)

re = Solution()
result = re.isPalindrome(a)
print(result)
