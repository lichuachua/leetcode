# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTargetNode(self, root: Optional[TreeNode], cnt: int) -> int:
        if root is None:
            return 0
        stack = []
        count = 0
        while len(stack) > 0 or root is not None:
            while root is not None:  # 走到最右边
                stack.append(root)  # 将当前树的根节点入栈
                root = root.right  # 找到最右侧节点
            root = stack.pop()  # 遍历到最右侧，当前节点无右子树时，将最右侧节点弹出
            count += 1
            if count == cnt:
                return root.val
            root = root.left  # 尝试访问该节点的左子树（可能最末尾没有右结点，但是存在左结点）
        return 0


"""
Solution：迭代
类似 230
已知中序遍历「左 -> 根 -> 右」能得到递增序列。逆中序遍历「右 -> 根 -> 左」可以得到递减序列。
则根据「右 -> 根 -> 左」迭代遍历 k 次，找到第k 个节点位置，并记录答案。
"""
