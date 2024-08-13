# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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


"""
l代
使用队列来存储每一层的元素
队列特征：先进先出，树的每层从左到右
先使用一个队列保存当前层元素，之后根据当前层元素，存储当前层元素保存在结果中后，
取出左右结点，存储到新队列中，便于下次遍历

需要在level为偶数时候，进行逆序
"""
