# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def trainingPlan(self, head: Optional[ListNode], cnt: int) -> Optional[ListNode]:
        # 可能是第一个节点，需要设置前置节点
        tmp = ListNode(0, head)
        fast, slow = head, tmp
        for i in range(cnt):
            fast = fast.next
        while fast is not None:
            slow = slow.next
            fast = fast.next
        return slow.next
