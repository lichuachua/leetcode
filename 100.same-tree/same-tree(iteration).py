# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pQueue, qQueue = [p], [q]
        while len(pQueue) > 0 and len(qQueue) > 0:
            pp, qq = pQueue[0], qQueue[0]
            pQueue.pop(0)
            qQueue.pop(0)
            if pp is None and qq is None:
                continue
            elif pp is None or qq is None or pp.val != qq.val:
                return False
            else:
                pQueue.append(pp.left)
                pQueue.append(pp.right)
                qQueue.append(qq.left)
                qQueue.append(qq.right)
        return True


"""
Solution：迭代
使用遍历（深度或者广度）比较遍历结点。
"""
