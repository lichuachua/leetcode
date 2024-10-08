# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is not None:
            return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
        else:
            return []


a, b, c = TreeNode(1), TreeNode(2), TreeNode(3)
a.left = None
a.right = b
b.left = c
b.right = None
c.right = None
c.left = None

re = Solution()
print(re.postorderTraversal(a))
