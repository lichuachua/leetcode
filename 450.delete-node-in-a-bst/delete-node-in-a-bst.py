# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root
        else:
            # 找到了要删除的节点
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            curr = root.right
            while curr.left:
                curr = curr.left
            curr.left = root.left
            return root.right


"""
Solution：递归
递归查找节点：通过比较 key 和 root.val，递归地在左子树或右子树中查找要删除的节点。
删除节点：
如果节点没有子节点，直接返回 None。
如果节点只有一个子节点，返回该子节点替代当前节点。
如果节点有两个子节点，找到右子树的最小值节点（中序后继），
则将左子树转移到右子树最左侧的叶子节点位置上，然后右子树代替当前节点位置。返回右子树。
返回结果：最终返回处理后的树的根节点。
"""
