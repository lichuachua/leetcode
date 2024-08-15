# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root
        else:
            # 找到了要删除的节点
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            curr = root.right
            while curr.left:
                curr = curr.left
            curr.left = root.left
            return root.right

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root is None:
            return result
        queue = [root]
        while len(queue) > 0:
            level = []
            currentQueue = queue
            queue = []
            for item in currentQueue:
                if item is None:
                    level.append(None)
                else:
                    level.append(item.val)
                    queue.append(item.left)
                    queue.append(item.right)
            # 删除全部结点都是None的一行，叶子结点的下一行
            if not all(element is None for element in level):
                result.append(level)

        return [item for sublist in result for item in sublist]


a, b, c, d, e, f = TreeNode(5), TreeNode(3), TreeNode(6), TreeNode(2), TreeNode(4), TreeNode(7)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
c.left = None
d.right = None
d.left = None
e.right = None
e.left = None
f.right = None
f.left = None

re = Solution()
print(re.levelOrder(a))
res = re.deleteNode(a, 3)
print(re.levelOrder(res))
