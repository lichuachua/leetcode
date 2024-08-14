# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode], min_v, max_v) -> bool:
        if root == None:
            return True
        if root.val >= max_v or root.val <= min_v:
            return False
        return self.preorderTraversal(root.left, min_v, root.val) and self.preorderTraversal(root.right, root.val,
                                                                                             max_v)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.preorderTraversal(root, float('-inf'), float('inf'))


"""
Solution：递归
二叉搜索树特征：
节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

根据题意进行递归遍历即可。前序、中序、后序遍历都可以。此处以前序遍历为例子。
在遍历子树时候，需要判断的是：
当前结点的左子树，只包含小于当前节点的数。但是当前结点的左子树的右子树，需要大于当前结点，并且小于当前结点的父结点
当前结点的右子树，只包含大于当前节点的数。但是当前结点的右子树的左子树，需要小于当前结点，并且大于当前结点的父结点

二叉搜索树中序遍历是有序的数组
"""
