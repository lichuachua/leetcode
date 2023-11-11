# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 先层次再转
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root is None:
            return result
        queue = [root]
        while len(queue) > 0:
            level = []
            currentQueue = queue
            queue = []
            for item in currentQueue:
                level.append(item.val)
                if item.left is not None:
                    queue.append(item.left)
                if item.right is not None:
                    queue.append(item.right)
            result.insert(0, level)
        return result
