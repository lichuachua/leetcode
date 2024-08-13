# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 使用层次遍历
        result = 0
        if root is None:
            return result
        queue = [root]
        while len(queue) > 0:
            currentQueue = queue
            queue = []
            for item in currentQueue:
                if item.left is not None:
                    queue.append(item.left)
                if item.right is not None:
                    queue.append(item.right)
            result += 1
        return result


"""
Solution：迭代
广度搜索可以直接计算当前树的层级，
同103，在遍历过程中，层树+1，则结果+1，不需要存储每一层的元素
"""
