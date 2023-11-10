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
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(2)

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
    def isSymmetric(self, root) -> bool:
        leftQ, rightQ = [root.left], [root.right]
        while len(leftQ) > 0 and len(rightQ) > 0:
            l, r = leftQ.pop(0), rightQ.pop(0)
            if not (l or r):
                continue
            if not (l and r):
                return False
            if l.val != r.val:
                return False
            leftQ.extend([l.left, l.right])
            rightQ.extend([r.right, r.left])

        if len(leftQ) == 0 and len(rightQ) == 0:
            return True
        else:
            return False


re = Solution()
print(re.isSymmetric(binary_tree_root))
