# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 伪前序
        # 前序-根左右；伪前序-根右左；后序-左右根
        res = []
        if root is None:
            return res
        stack = [root]
        while len(stack) > 0:
            root = stack[len(stack) - 1]
            stack.pop()
            res.append(root.val)
            # 栈是逆序
            if root.left is not None:
                stack.append(root.left)
            if root.right is not None:
                stack.append(root.right)

        i, j = 0, len(res) - 1
        while i < j:
            res[i], res[j] = res[j], res[i]
            i += 1
            j -= 1
        return res
