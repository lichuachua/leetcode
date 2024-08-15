# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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


"""
已知中序遍历「左 -> 根 -> 右」能得到递增序列。逆中序遍历「右 -> 根 -> 左」可以得到递减序列。
则根据「右 -> 根 -> 左」递归遍历 k 次，找到第k 个节点位置，并记录答案。
"""
