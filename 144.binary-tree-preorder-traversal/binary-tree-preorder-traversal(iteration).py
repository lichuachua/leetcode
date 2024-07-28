# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root is None:
            return res
        stack = [root]
        while len(stack) > 0:
            root = stack[len(stack) - 1]
            stack.pop()
            res.append(root.val)
            # 栈是逆序
            if root.right is not None:
                stack.append(root.right)
            if root.left is not None:
                stack.append(root.left)
        return res


"""
Solution：迭代+栈
通过迭代调用根->左->右的顺序实现二叉树的前序遍历
使用栈是因为栈先进后出的性质，入栈的顺序应该为：先放入右子树，再放入左子树。这样可以保证最终为前序遍历顺序（出栈顺序为先左再右）。
二叉树的前序遍历显式栈实现步骤如下：

执行
判断二叉树是否为空，为空则直接返回。
初始化维护一个栈，将根节点入栈。
当栈不为空时：
弹出栈顶元素 node，并访问该元素。
如果 node 的右子树不为空，则将 node 的右子树入栈。
如果 node 的左子树不为空，则将 node 的左子树入栈。
"""
