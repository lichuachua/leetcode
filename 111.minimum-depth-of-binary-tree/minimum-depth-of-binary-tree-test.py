# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is not None:
            return self.minDepth(root.right) + 1
        if root.right is None and root.left is not None:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


a, b, c, d, e = TreeNode(3), TreeNode(9), TreeNode(20), TreeNode(15), TreeNode(17)
a.left = b
a.right = c
b.left = None
b.right = None
c.left = d
c.right = e
d.left = None
d.right = None
e.left = None
e.right = None

re = Solution()
print(re.minDepth(a))
