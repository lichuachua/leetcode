# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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


a, b, c = TreeNode(1), TreeNode(2), TreeNode(3)
a.left = b
a.right = c
b.left = None
b.right = None
c.left = None
c.right = None

ser = Codec()
deser = Codec()
print(ser.serialize(a))
ans = deser.deserialize(ser.serialize(a))
print(ans.val)
