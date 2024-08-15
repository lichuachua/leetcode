# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    res = 0
    k = 0

    def lcc(self, root: Optional[TreeNode]):
        if root is None:
            return
        self.lcc(root.right)
        if self.k == 0:
            return
        self.k -= 1
        if self.k == 0:
            self.res = root.val
            return
        self.lcc(root.left)

    def findTargetNode(self, root: Optional[TreeNode], cnt: int) -> int:
        self.res = 0
        self.k = cnt
        self.lcc(root)
        return self.res


a, b, c, d, e = TreeNode(7), TreeNode(3), TreeNode(9), TreeNode(1), TreeNode(5)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = None
c.left = None
d.right = None
d.left = None
e.right = None
e.left = None

re = Solution()
res = re.findTargetNode(a, 2)
print(res)
