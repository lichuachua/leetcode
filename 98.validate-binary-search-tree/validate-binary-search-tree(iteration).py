# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root is None:
            return res
        stack = []
        while len(stack) > 0 or root is not None:
            while root is not None:  # 走到最左边
                stack.append(root)  # 将当前树的根节点入栈
                root = root.left  # 找到最左侧节点
            root = stack[len(stack) - 1]  # 取最左元素
            # 新加的，判断是否有序
            if len(res) > 0 and root.val <= res[-1]:
                return False

            res.append(root.val)
            stack.pop()  # 遍历到最左侧，当前节点无左子树时，将最左侧节点弹出
            root = root.right  # 尝试访问该节点的右子树（可能最末尾没有左结点，但是存在右结点）
        return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.inorderTraversal(root)


"""
Solution：迭代
二叉搜索树特征：
节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
迭代遍历 树的中序遍历，二叉搜索树中序遍历是是有序的数组。
中序遍历参考94
"""
