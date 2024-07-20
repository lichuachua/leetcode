"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        m = {}
        cur = head
        while cur:
            new_node = Node(cur.val, None, None)
            m[cur] = new_node
            cur = cur.next
        cur = head

        while cur:
            if cur.next:
                m[cur].next = m[cur.next]
            if cur.random:
                m[cur].random = m[cur.random]
            cur = cur.next
        return m[head]


"""
Solution:哈希表
遍历链表，利用哈希表，以 旧节点: 新节点 为映射关系，将节点关系存储下来。 
再次遍历链表，将新链表的 next 和 random 指针设置好。
"""
