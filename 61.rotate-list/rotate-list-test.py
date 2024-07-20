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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 0:
            return head
        tmp = head
        count = 1
        while head.next is not None:
            head = head.next
            count += 1
        head.next = tmp
        i = 1
        k %= count
        while i < count - k:
            tmp = tmp.next
            i += 1
        result = tmp.next
        tmp.next = None
        return result


e = ListNode(5, None)
d = ListNode(4, e)
c = ListNode(3, d)
b = ListNode(2, c)
a = ListNode(1, b)

re = Solution()
result = re.rotateRight(a, 2)
while result:
    print(result.val)
    result = result.next
