# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createTree(self, preorder: List[int], inorder: List[int], n: int) -> TreeNode:
        if n == 0:
            return None
        # 找到当前前序遍历的第一个节点在中序遍历中的位置
        k = 0
        while preorder[0] != inorder[k]:
            k += 1
        # 当前节点的值是中序遍历中的第 k 个元素
        node = TreeNode(inorder[k])
        # 递归构建左子树
        # preorder[1: k+1] 是当前节点左子树的前序遍历
        # inorder[0: k] 是当前节点左子树的中序遍历
        node.left = self.createTree(preorder[1: k + 1], inorder[0: k], k)
        # 递归构建右子树
        # preorder[k+1:] 是当前节点右子树的前序遍历
        # inorder[k+1:] 是当前节点右子树的中序遍历
        node.right = self.createTree(preorder[k + 1:], inorder[k + 1:], n - k - 1)
        return node

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.createTree(preorder, inorder, len(inorder))


"""
Solution：递归
前序遍历的顺序是：根 -> 左 -> 右。中序遍历的顺序是：左 -> 根 -> 右。
根据前序遍历的顺序，可以找到根节点位置。然后在中序遍历的结果中可以找到对应的根节点位置，
就可以从根节点位置将二叉树分割成左子树、右子树。同时能得到左右子树的节点个数。
此时构建当前节点，并递归建立左右子树，在左右子树对应位置继续递归遍历进行上述步骤，直到节点为空，
"""
