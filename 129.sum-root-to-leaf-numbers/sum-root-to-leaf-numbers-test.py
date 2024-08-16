# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, root: Optional[TreeNode], pre_total: int) -> int:
        if root is None:
            return 0
        total = pre_total * 10 + root.val
        if root.left is None and root.right is None:
            return total
        return self.dfs(root.left, total) + self.dfs(root.right, total)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)


a, b, c = TreeNode(1), TreeNode(2), TreeNode(3)
a.left = b
a.right = c
b.left = None
b.right = None
c.left = None
c.right = None

re = Solution()
print(re.sumNumbers(a))
