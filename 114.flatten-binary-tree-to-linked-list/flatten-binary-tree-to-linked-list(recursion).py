# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcc(self, node: Optional[TreeNode]) -> TreeNode:
        if node is None:
            return None
        left_tail = self.lcc(node.left)
        right_tail = self.lcc(node.right)
        if left_tail is not None:
            left_tail.right = node.right
            node.right = node.left
            node.left = None
        if right_tail is not None:
            return right_tail
        if left_tail is not None:
            return left_tail
        return node

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        return self.lcc(root)


"""
Solution：递归
递归方法的关键思路是：
递归遍历：按照前序遍历的方式递归地展开左子树和右子树。
重组树结构：将左子树展开后连接到当前节点的右侧，然后将右子树连接到左子树展开后的链表末尾。
"""
