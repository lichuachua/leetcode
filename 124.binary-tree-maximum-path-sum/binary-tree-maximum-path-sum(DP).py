# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float('-inf')

        def dfs(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            left_max = max(dfs(root.left), 0)  # 左子树提供的最大贡献值
            right_max = max(dfs(root.right), 0)  # 右子树提供的最大贡献值

            cur_max = left_max + right_max + root.val  # 包含当前节点和左右子树的最大路径和
            self.ans = max(self.ans, cur_max)  # 更新所有路径中的最大路径和

            return max(left_max, right_max) + root.val  # 返回包含当前节点的子树的最大贡献值

        dfs(root)
        return self.ans


"""
Solution：树形 DP + 深度优先搜索
根据最大路径和中对应路径是否穿过根节点，我们可以将二叉树分为两种：
    最大路径和中对应路径穿过根节点。
    最大路径和中对应路径不穿过根节点。
如果最大路径和中对应路径穿过根节点，则：该二叉树的最大路径和 = 左子树中最大贡献值 + 右子树中最大贡献值 + 当前节点值。
而如果最大路径和中对应路径不穿过根节点，则：该二叉树的最大路径和 = 所有子树中最大路径和。

即：该二叉树的最大路径和 = max(左子树中最大贡献值 + 右子树中最大贡献值 + 当前节点值，所有子树中最大路径和)。

对此我们可以使用深度优先搜索递归遍历二叉树，并在递归遍历的同时，维护一个最大路径和变量 ans。

然后定义函数 def dfs(self, node): 计算二叉树中以该节点为根节点，并且经过该节点的最大贡献值。
计算的结果可能的情况有 2 种：
    经过空节点的最大贡献值等于0。
    经过非空节点的最大贡献值等于 当前节点值 + 左右子节点提供的最大贡献值中较大的一个。如果该贡献值为负数，可以考虑舍弃，即最大贡献值为 0。
"""
