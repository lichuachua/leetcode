# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        # 快慢指针--快指针走两步，慢指针走一步，若存在环，迟早快慢指针相遇，若快指针到链表末尾，则无环
        slow, fast = head, head.next  # 如果slow和fast都为head，则fast==slow，直接return true了
        while fast != slow:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
