# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


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

a1, b1, c1, d1, e1 = TreeNode(3), TreeNode(9), TreeNode(20), TreeNode(15), TreeNode(17)
a1.left = b1
a1.right = c1
b1.left = None
b1.right = None
c1.left = d1
c1.right = e1
d1.left = None
d1.right = None
e1.left = None
e1.right = None

re = Solution()
print(re.isSameTree(a, a1))
