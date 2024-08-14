# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p or root == q:
            return root
        if root is not None:
            node_left = self.lowestCommonAncestor(root.left, p, q)
            node_right = self.lowestCommonAncestor(root.right, p, q)
            if node_left is not None and node_right is not None:
                return root
            elif node_left is None:
                return node_right
            else:
                return node_left
        return None


a, b, c = TreeNode(1), TreeNode(2), TreeNode(3)
a.left = b
a.right = c
b.left = None
b.right = None
c.left = None
c.right = None

re = Solution()
res = re.lowestCommonAncestor(a, b, c)
print(res.val)
