
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root is None:
            return res

        def iteration(root, level):
            if root is None:
                return root
            if len(res) == level:
                res.append([])
            res[level].append(root.val)
            iteration(root.left, level + 1)
            iteration(root.right, level + 1)

        iteration(root, 0)
        return res
