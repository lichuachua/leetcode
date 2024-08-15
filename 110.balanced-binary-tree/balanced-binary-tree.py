# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)
        if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
            return -1
        else:
            return max(leftHeight, rightHeight) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root) >= 0


"""
Solution：递归
先递归遍历左右子树，判断左右子树是否平衡，再判断以当前节点为根节点的左右子树是否平衡。
如果遍历的子树是平衡的，则返回它的高度，否则返回 -1。
只要出现不平衡的子树，则该二叉树一定不是平衡二叉树。

height 函数：
这是一个递归函数，用于计算当前节点的高度。
如果当前节点为空，返回高度为 0。
递归计算左右子树的高度。如果某个子树不平衡（返回 -1），或者当前节点的左右子树高度差超过 1，直接返回 -1 表示该树不平衡。
如果左右子树都平衡，则返回当前节点的高度（即左右子树高度的最大值加上 1）。
"""
