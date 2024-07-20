# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        m = {}
        while head is not None:
            if head in m:
                return head
            m[head] = True
            head = head.next
        return None


"""
Solution: hash map
和141一样
遍历所有节点，每次遍历节点之前，使用哈希表判断该节点是否被访问过。
如果访问过就说明存在环，如果没访问过则将该节点添加到哈希表中，继续遍历判断。
"""
