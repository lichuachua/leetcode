# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
            if len(result) % 2 != 0:
                level.reverse()
            result.append(level)  # Append the current level to the result
        return result


a, b, c = TreeNode(1), TreeNode(2), TreeNode(3)
a.left = None
a.right = b
b.left = c
b.right = None
c.right = None
c.left = None

re = Solution()
print(re.zigzagLevelOrder(a))
