# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
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
        result = [row[-1] for row in res]

        return result


"""
Solution：递归
同102
使用广度优先搜索对二叉树进行层次遍历。在遍历每层节点的时候，只需要将最后一个节点加入结果数组即可。
"""
