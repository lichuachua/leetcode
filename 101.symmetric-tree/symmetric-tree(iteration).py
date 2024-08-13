# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        leftQ, rightQ = [root.left], [root.right]
        while len(leftQ) > 0 and len(rightQ) > 0:
            l, r = leftQ.pop(0), rightQ.pop(0)
            if l is None and r is None:
                continue
            elif l is None or r is None or r.val != l.val:
                return False
            leftQ.extend([l.left, l.right])
            rightQ.extend([r.right, r.left])

        if len(leftQ) == 0 and len(rightQ) == 0:
            return True
        else:
            return False


"""
Solution：迭代

通过两个队列同时遍历树的左右子树，比较每一层的节点，确保节点值相等，并且左右子树的结构是镜像对称的。
使用队列 leftQ 和 rightQ 记录当前需要检查的节点。
通过反向插入的方式，确保在每一层上，左子树的左子节点与右子树的右子节点配对检查，左子树的右子节点与右子树的左子节点配对检查。

"""
