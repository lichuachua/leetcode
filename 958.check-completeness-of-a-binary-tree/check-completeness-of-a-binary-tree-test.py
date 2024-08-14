# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        queue = [root]
        end = False  # 标记是否遇到空节点

        while len(queue) > 0:
            node = queue.pop(0)  # 从队列的开头移除节点

            if node is not None:
                if end:
                    return False
                queue.append(node.left)
                queue.append(node.right)
            else:
                end = True  # 遇到空节点后，标记后续节点必须为 None

        return True


a, b, c, d, e, f = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(6)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = None
d.left = None
d.right = None
e.left = None
e.right = None
f.left = None
f.right = None

re = Solution()
print(re.isCompleteTree(a))
