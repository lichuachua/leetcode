# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfNumbers(self, grid: List[List[int]]) -> int:
        total_sum = 0

        for row in grid:
            # 将每个一维数组转换为数字
            number = int("".join(map(str, row)))
            total_sum += number

        return total_sum

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # 初始化存储路径的结果列表
        res = []

        def dfs(node: TreeNode, path: List[int]):
            if not node:
                return

            # 将当前节点值加入路径
            path.append(node.val)

            # 如果是叶子节点，保存当前路径的拷贝
            if not node.left and not node.right:
                res.append(path[:])
            else:
                # 继续递归遍历左子树和右子树
                dfs(node.left, path)
                dfs(node.right, path)

            # 回溯：撤销当前节点的选择
            path.pop()

        # 从根节点开始 DFS
        dfs(root, [])
        # 现在的res是所有的路径

        return self.sumOfNumbers(res)


"""
Solution：递归+深度优先搜索
类似112 113
递归保存每条路径，之后进行相加
"""
