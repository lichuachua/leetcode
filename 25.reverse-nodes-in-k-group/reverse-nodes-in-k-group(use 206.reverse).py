# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 原地反转-头插法
        result = None
        tmp = None
        while head:
            tmp = head.next
            head.next = result
            result = head
            head = tmp
        return result

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
            # 因为从0开始算的
            end = prev
            for _ in range(k):
                end = end.next

            next_start = end.next
            end.next = None  # Temporarily break the chain

            # Reverse the sublist
            reversed_list = self.reverseList(start)

            # Connect the reversed sublist back to the main list
            prev.next = reversed_list

            start.next = next_start
            prev = start

            count -= k

        return dummy.next
