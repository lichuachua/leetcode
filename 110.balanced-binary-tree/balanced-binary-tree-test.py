from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_binary_tree():
    # 创建节点
    root = TreeNode(1)

    return root


def print_binary_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left is not None or root.right is not None:
            print_binary_tree(root.left, level + 1, "L--- ")
            print_binary_tree(root.right, level + 1, "R--- ")


# 构建二叉树
binary_tree_root = build_binary_tree()

# 打印二叉树
print_binary_tree(binary_tree_root)

class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None :
            return True
        def maxDepth(root):
            if root is None:
                return True
            return max(maxDepth(root.left), maxDepth(root.right)) + 1
        level = abs(maxDepth(root.right)-maxDepth(root.left))
        if level <= 1 :
            return True
        else:
            return False

re = Solution()
print(re.isBalanced(binary_tree_root))
