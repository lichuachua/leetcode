# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        m = {}
        while headA:
            m[headA] = True
            headA = headA.next
        while headB:
            if headB in m:
                return headB
            headB = headB.next
        return None


"""
Solution: hash map
分别遍历两个链表，
遍历链表A，使用哈希表存储该节点是否被访问过。
遍历链表B，如果访问过就说明相交，直接return
"""
