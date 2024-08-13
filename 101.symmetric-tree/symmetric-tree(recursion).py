# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcc(self, left, right):
        if left is None and right is None:
            return True
        elif left is None or right is None or right.val != left.val:
            return False
        return self.lcc(left.right, right.left) & self.lcc(left.left, right.right)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.lcc(root.left, root.right)

"""
Solution：递归
使用递归遍历结点的左子树和右子树是否存在，且值相等，如果不成立，说明不对称
如果成立，则递归遍历左子树的右结点和右子树的左结点，以及右子树的右结点和左子树的左结点是否一
"""