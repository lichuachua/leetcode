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

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


a, b, c, d, e = TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(1), TreeNode(2)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = None
c.right = None
d.left = None
d.right = None
e.left = None
e.right = None

a1, b1, c1, = TreeNode(4), TreeNode(1), TreeNode(2)
a1.left = b1
a1.right = c1
b1.left = None
b1.right = None
c1.left = None
c1.right = None

re = Solution()
print(re.isSubtree(a, a1))
