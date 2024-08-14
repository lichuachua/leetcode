from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
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


a, b, c, d, e = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(15), TreeNode(17)
a.left = b
a.right = c
b.left = None
b.right = None
c.left = None
c.right = None

re = Solution()
print(re.pathSum(a,5))
