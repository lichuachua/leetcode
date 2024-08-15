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
        self.lcc(root.left)
        if self.k==0:
            return
        self.k -=1
        if self.k==0:
            self.res = root.val
            return
        self.lcc(root.right)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.lcc(root)
        return self.res

"""
Solution:递归
类似 230
已知中序遍历「左 -> 根 -> 右」能得到递增序列。逆中序遍历「右 -> 根 -> 左」可以得到递减序列。
则根据「右 -> 根 -> 左」递归遍历 k 次，找到第k 个节点位置，并记录答案。
"""
