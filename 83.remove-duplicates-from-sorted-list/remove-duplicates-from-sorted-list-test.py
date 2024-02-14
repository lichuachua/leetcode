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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        tmp = head
        while tmp.next is not None:
            if tmp.val == tmp.next.val:
                tmp.next = tmp.next.next
            else:
                tmp = tmp.next
        return head


c = ListNode(2, None)
b = ListNode(1, c)
a = ListNode(1, b)

re = Solution()
result = re.deleteDuplicates(a)
while result is not None:
    print(result.val)
    result = result.next
