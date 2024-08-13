# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is not None:
            return self.minDepth(root.right) + 1
        if root.right is None and root.left is not None:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


"""
Solution：递归
同104题，通过递归计算左右子树的最小深度，之后选择二者中最小的，由于跟结点算1个所以吸引结果+1
与104不同的是，
如果左子树为空但右子树非空（没有左子树，最小深度只能通过右子树得到，空树没深度），递归计算右子树的最小深度并加1
如果右子树为空但左子树非空同上。

"""
