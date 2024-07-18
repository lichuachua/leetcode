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


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        start = prev.next
        then = start.next

        for _ in range(right - left):
            start.next = then.next
            then.next = prev.next
            prev.next = then
            then = start.next

        return dummy.next

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        count = 0

        # Count the number of nodes in the list
        while current.next:
            current = current.next
            count += 1

        prev = dummy

        while count >= k:
            start = prev.next
            end = prev
            for _ in range(k):
                end = end.next

            next_start = end.next
            end.next = None  # Temporarily break the chain

            # Reverse the sublist
            reversed_list = self.reverseBetween(start, 1, k)

            # Connect the reversed sublist back to the main list
            prev.next = reversed_list

            start.next = next_start
            prev = start

            count -= k

        return dummy.next


e = ListNode(5, None)
d = ListNode(4, e)
c = ListNode(3, d)
b = ListNode(2, c)
a = ListNode(1, b)

re = Solution()
result = re.reverseKGroup(a, 2)
while result:
    print(result.val)
    result = result.next
