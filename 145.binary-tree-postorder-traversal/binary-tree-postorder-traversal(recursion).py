# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is not None:
            return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
        else:
            return []


"""
Solution：递归
通过递归调用左->右->根的顺序实现二叉树的后序遍历
"""
