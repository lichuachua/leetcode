# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createTree(self, inorder: List[int], postorder: List[int], n: int) -> TreeNode:
        if n == 0:
            return None
        # 找到当前后序遍历的最后一个节点在中序遍历中的位置
        k = 0
        while postorder[-1] != inorder[k]:
            k += 1
        # 当前节点的值是中序遍历中的第 k 个元素
        node = TreeNode(inorder[k])
        # 递归构建左子树
        # preorder[1: k+1] 是当前节点左子树的前序遍历
        # inorder[0: k] 是当前节点左子树的中序遍历
        node.left = self.createTree(inorder[0: k], postorder[0: k], k)
        # 递归构建右子树
        # preorder[k+1:] 是当前节点右子树的前序遍历
        # inorder[k+1:] 是当前节点右子树的中序遍历
        node.right = self.createTree(inorder[k + 1:], postorder[k:n - 1], n - k - 1)
        return node

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.createTree(inorder, postorder, len(inorder))

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root is None:
            return result
        queue = [root]
        while len(queue) > 0:
            level = []
            currentQueue = queue
            queue = []
            for item in currentQueue:
                if item is None:
                    level.append(None)
                else:
                    level.append(item.val)
                    queue.append(item.left)
                    queue.append(item.right)
            # 删除全部结点都是None的一行，叶子结点的下一行
            if not all(element is None for element in level):
                result.append(level)

        return [item for sublist in result for item in sublist]


re = Solution()
root = re.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
print(re.levelOrder(root))
"""
展示结果需要用到
层次遍历，如102，以上会显示None的结点，当然，叶子结点的none不会显示
"""
