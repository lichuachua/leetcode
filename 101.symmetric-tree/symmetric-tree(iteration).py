# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root) -> bool:
        leftQ, rightQ = [root.left], [root.right]
        while len(leftQ) > 0 and len(rightQ) > 0:
            l, r = leftQ.pop(0), rightQ.pop(0)
            if not (l or r):
                continue
            if not (l and r):
                return False
            if l.val != r.val:
                return False
            leftQ.extend([l.left, l.right])
            rightQ.extend([r.right, r.left])

        if len(leftQ) == 0 and len(rightQ) == 0:
            return True
        else:
            return False
