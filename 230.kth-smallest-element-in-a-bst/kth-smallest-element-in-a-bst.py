# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        if root is None:
            return res
        stack = []
        while len(stack) > 0 or root is not None:
            while root is not None:  # 走到最左边
                stack.append(root)  # 将当前树的根节点入栈
                root = root.left  # 找到最左侧节点
            root = stack[len(stack) - 1]  # 取最左元素
            k -= 1
            if k == 0:
                return root.val
            res.append(root.val)
            stack.pop()  # 遍历到最左侧，当前节点无左子树时，将最左侧节点弹出
            root = root.right  # 尝试访问该节点的右子树（可能最末尾没有左结点，但是存在右结点）
        return 0


a, b, c, d = TreeNode(3), TreeNode(1), TreeNode(4), TreeNode(2)
a.left = b
a.right = c
c.right = d
c.left = None
d.right = None
d.left = None

re = Solution()
res = re.kthSmallest(a, 1)
print(res)
