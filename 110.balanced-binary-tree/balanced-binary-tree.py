# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def maxDepth(root):
            if root is None:
                return True
            return max(maxDepth(root.left), maxDepth(root.right)) + 1

        level = abs(maxDepth(root.right) - maxDepth(root.left))
        return level <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
