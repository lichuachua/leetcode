# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
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
            result.append(level[-1])
        return result


"""
Solution：迭代
同102
使用广度优先搜索对二叉树进行层次遍历。在遍历每层节点的时候，只需要将最后一个节点加入结果数组即可。
"""
