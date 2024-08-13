# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            return sum == root.val
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)


"""
Solution：递归
递归遍历从跟结点到左右子树的结点。
根结点为空，（还没到sum，但是已经没有结点），返回false
根结点为叶子结点，返回路径是否相等
递归遍历当前结点和剩余的sum（原sum-结点的val）
"""
