# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            return sum == root.val
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)


a, b, c, d, e = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(15), TreeNode(17)
a.left = b
a.right = c
b.left = None
b.right = None
c.left = None
c.right = None

re = Solution()
print(re.hasPathSum(a, 5))
