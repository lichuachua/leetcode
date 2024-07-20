"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


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


a = Node(7)
b = Node(13)
c = Node(11)
d = Node(10)
e = Node(1)

a.next = b
b.next = c
c.next = d
d.next = e

b.random = a
c.random = e
d.random = c
e.random = a

re = Solution()
result = re.copyRandomList(a)
while result:
    print(result.val)
    result = result.next
