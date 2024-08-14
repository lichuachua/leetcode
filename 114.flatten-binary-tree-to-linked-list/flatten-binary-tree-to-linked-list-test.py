# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lcc(self, node: Optional[TreeNode]) -> TreeNode:
        if node is None:
            return None
        left_tail = self.lcc(node.left)
        right_tail = self.lcc(node.right)
        if left_tail is not None:
            left_tail.right = node.right
            node.right = node.left
            node.left = None
        if right_tail is not None:
            return right_tail
        if left_tail is not None:
            return left_tail
        return node

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        return self.lcc(root)


a, b, c, d, e, f = TreeNode(1), TreeNode(2), TreeNode(5), TreeNode(3), TreeNode(4), TreeNode(6)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = None
c.right = f
d.left = None
d.right = None
e.left = None
e.right = None
f.left = None
f.right = None

re = Solution()
result = re.flatten(a)
current = a
while current:
    print(current.val, end=" -> " if current.right else "\n")
    current = current.right
