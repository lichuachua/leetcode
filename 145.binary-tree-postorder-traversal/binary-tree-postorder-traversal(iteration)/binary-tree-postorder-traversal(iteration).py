# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root is None:
            return res
        stack = []
        # 前置保存右节点的根
        preRight = None
        while len(stack) > 0 or root is not None:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack[len(stack) - 1]
            stack.pop()
            # 如果右子树不存在 或 右子树已经被访问过：可以将节点值加入结果列表。
            # 否则：将当前节点重新入栈，并将 root 更新为右子树进行处理。
            if root.right is None or root.right == preRight:
                res.append(root.val)
                preRight = root
                root = None
            else:
                stack.append(root)
                root = root.right
        return res


"""
Solution：迭代+栈
通过迭代调用左->右->根的顺序实现二叉树的后序遍历
同中序遍历一样，向左遍历：将所有左子树节点推入栈中。
处理节点：
如果右子树不存在 或 右子树已经被访问过：可以将节点值加入结果列表。
否则：将当前节点重新入栈，并将 root 更新为右子树进行处理。
"""
