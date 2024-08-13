from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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
print(re.maxPathSum(a))
