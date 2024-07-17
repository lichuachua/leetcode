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


e = ListNode(5, None)
d = ListNode(4, e)
c = ListNode(3, d)
b = ListNode(2, c)
a = ListNode(1, b)

re = Solution()
result = re.reverseBetween(a, 2, 4)
while result:
    print(result.val)
    result = result.next
