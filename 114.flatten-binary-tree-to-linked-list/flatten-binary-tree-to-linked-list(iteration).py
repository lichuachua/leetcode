# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        stack = [root]
        prev = None
        while len(stack) > 0:
            node = stack.pop()
            if prev is not None:
                prev.left = None
                prev.right = node
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            prev = node


"""
Solution：迭代

迭代方法的关键思路是：
使用栈：通过栈来模拟前序遍历，依次处理当前节点。
重组树结构：将当前节点的左子树处理后连接到右侧。
    对于当前处理的节点，如果 prev 存在，将其右子节点设置为当前节点，左子节点设置为 None。
    更新 prev 为当前节点。
"""
