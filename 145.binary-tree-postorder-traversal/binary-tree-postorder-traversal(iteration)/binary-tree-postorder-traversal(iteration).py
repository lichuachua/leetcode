# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root is None:
            return res
        stack = []
        # 前置保存右节点的根
        preRight = None
        while len(stack) > 0 or root is not None:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack[len(stack) - 1]
            stack.pop()
            if root.right is None or root.right == preRight:
                res.append(root.val)
                preRight = root
                root = None
            else:
                stack.append(root)
                root = root.right
        return res
