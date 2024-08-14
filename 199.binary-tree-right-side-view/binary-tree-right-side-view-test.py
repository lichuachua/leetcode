from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


a, b, c, d, e = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(5), TreeNode(4)
a.left = b
a.right = c
b.left = None
b.right = d
c.left = None
c.right = e
d.left = None
d.right = None
e.left = None
e.right = None

re = Solution()
print(re.rightSideView(a))
