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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 使用三个指针
        res = ListNode(0,head)
        pre = res
        while head is not None and head.next is not None:
            slow,fast = head,head.next
            pre.next = fast
            slow.next = fast.next
            fast.next = slow
            pre,head = slow,slow.next
        return res.next

e = ListNode(5, None)
d = ListNode(4, e)
c = ListNode(3, d)
b = ListNode(2, c)
a = ListNode(1, b)

re = Solution()
result = re.swapPairs(a)
while result is not None:
    print(result.val)
    result = result.next