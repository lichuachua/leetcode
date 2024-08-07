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
            res.append(root.val)
            stack.pop()  # 遍历到最左侧，当前节点无左子树时，将最左侧节点弹出
            root = root.right  # 尝试访问该节点的右子树（可能最末尾没有左结点，但是存在右结点）
        return res


"""
Solution：迭代+栈
通过迭代调用左->根->右的顺序实现二叉树的中序遍历
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
