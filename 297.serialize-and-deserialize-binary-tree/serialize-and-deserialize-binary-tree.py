# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is not None:
            return str(root.val) + ',' + str(self.serialize(root.left)) + ',' + str(self.serialize(root.right))
        else:
            return 'None'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def dfs(datalist):
            val = datalist.pop(0)
            if val == 'None':
                return None
            root = TreeNode(int(val))
            root.left = dfs(datalist)
            root.right = dfs(datalist)
            return root

        datalist = data.split(',')
        return dfs(datalist)

    # Your Codec object will be instantiated and called as such:


# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


"""
Solution：深度搜索前序
递归遍历
1. 序列化：将二叉树转为字符串数据表示
2. 反序列化：将字符串数据转为二叉树结构
"""
