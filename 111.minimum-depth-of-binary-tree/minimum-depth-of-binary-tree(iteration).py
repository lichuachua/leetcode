# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        result = 1
        queue = [root]
        while len(queue) > 0:
            currentQueue = queue
            queue = []
            for item in currentQueue:
                if item.left is None and item.right is None:
                    return result
                if item.left is not None:
                    queue.append(item.left)
                if item.right is not None:
                    queue.append(item.right)
            result += 1
        return result


"""
Solution：迭代
同104最大深度
同103，层次遍历在遍历过程中，层树+1，则结果+1，不需要存储每一层的元素。
与104不同的是，需要判断结点，如果左右都为空，直接返回结果

"""
