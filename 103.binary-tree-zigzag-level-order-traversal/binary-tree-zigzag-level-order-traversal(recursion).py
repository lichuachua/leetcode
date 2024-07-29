# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root is None:
            return res

        def iteration(root, level):
            if root is None:
                return root
            if len(res) == level:  # 新增的一层，初始化本层
                res.append([])
            res[level].append(root.val)  # 元素添加到当前层
            iteration(root.left, level + 1)  # 遍历下一层的左子树
            iteration(root.right, level + 1)  # 遍历下一层的右子树

        iteration(root, 0)

        result = []
        for level in range(len(res)):
            if level % 2 == 1:
                result.append(res[level][::-1])  # Reverse for odd levels
            else:
                result.append(res[level])

        return result


"""
Solution：递归
类似102。
102完成后，再次遍历res，偶数层逆序存储
"""
