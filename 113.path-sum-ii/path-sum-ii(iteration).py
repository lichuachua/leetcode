# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(root: TreeNode, targetSum: int):
            if root is None:
                return
            path.append(root.val)
            targetSum -= root.val
            if root.left is None and root.right is None:
                if targetSum == 0:
                    res.append(path[:])
            dfs(root.left, targetSum)
            dfs(root.right, targetSum)
            path.pop()  # 撤销了对当前节点的选择，回溯到父节点

        dfs(root, targetSum)
        return res


"""
Solution：递归
同112
递归遍历从跟结点到左右子树的结点。
根结点为空，（还没到sum，但是已经没有结点），返回空数组
根结点为叶子结点，返回路径是否相等，并且targetSum为0，则path为目标路径
递归遍历当前结点和剩余的sum

注意一个操作，【回溯到父节点】。
在处理完当前节点的所有子节点之后，你需要回到父节点进行其他可能的路径探索。
通过 path.pop() 从 path 列表中移除当前节点的值。
这一步骤撤销了对当前节点的选择，回到父节点，从而允许探索其他路径。
"""
