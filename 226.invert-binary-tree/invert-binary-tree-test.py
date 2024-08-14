# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        queue = [root]
        while len(queue) > 0:
            node = queue.pop(0)
            node.left, node.right = node.right, node.left
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return root


a, b, c, d, e = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(5), TreeNode(4)
a.left = b
a.right = c
b.left = None
b.right = d
c.left = None
c.right = e
d.left = None
d.right = None
e.left = None
e.right = None

re = Solution()
print(re.invertTree(a))
