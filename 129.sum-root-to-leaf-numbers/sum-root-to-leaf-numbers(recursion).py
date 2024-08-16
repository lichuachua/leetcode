# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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


"""
Solution：递归+深度优先搜索
类似112 113
记录下路径上所有节点构成的数字，使用变量 pre_total 保存下当前路径上构成的数字。
如果遇到叶节点，则直接返回当前数字。
如果没有遇到叶节点，则递归遍历左右子树，并累加对应结果。
"""
