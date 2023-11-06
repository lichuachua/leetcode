# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        while len(stack) > 0 or root is not None:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack[len(stack) - 1]
            res.append(root.val)
            stack.pop()
            root = root.right
        return res