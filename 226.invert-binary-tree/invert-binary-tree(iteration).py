# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        queue = [root]
        while len(queue) > 0:
            node = queue.pop(0)
            node.left, node.right = node.right, node.left
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return root


"""
Solution：迭代
使用队列存储结点。
遍历 反转当前结点的左右结点，之后将当前结点的左右结点入队。
其中        queue = [root]和            node = queue.pop(0)
可以换为        queue = deque([root])  # 使用 deque 作为队列     和            node = queue.popleft()  # 从队列的左端移除节点
"""
