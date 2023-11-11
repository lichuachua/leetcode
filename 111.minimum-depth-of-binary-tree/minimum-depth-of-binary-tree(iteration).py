# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # 使用层次遍历
        if root is None:
            return 0
        result = 1
        queue = [root]
        while len(queue) > 0:
            length = len(queue)
            i = 0
            while i < length:
                value = queue[0]
                queue = queue[1:]
                if value.left is None and value.right is None:
                    return result
                if value.left is not None:
                    queue.append(value.left)
                if value.right is not None:
                    queue.append(value.right)
                i += 1
            result += 1
        return result
