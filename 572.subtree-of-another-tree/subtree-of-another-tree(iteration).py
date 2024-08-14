# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pQueue, qQueue = [p], [q]
        while len(pQueue) > 0 and len(qQueue) > 0:
            pp, qq = pQueue[0], qQueue[0]
            pQueue.pop(0)
            qQueue.pop(0)
            if pp is None and qq is None:
                continue
            elif pp is None or qq is None or pp.val != qq.val:
                return False
            else:
                pQueue.append(pp.left)
                pQueue.append(pp.right)
                qQueue.append(qq.left)
                qQueue.append(qq.right)
        return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue = [root]
        while queue:
            node = queue.pop(0)
            if self.isSameTree(node, subRoot):
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False


"""
Solution：递归
类似100
遍历树中的每一个结点作为根结点，是否有和子树相同的

其中        queue = [root]和            node = queue.pop(0)
可以换为        queue = deque([root])  # 使用 deque 作为队列     和            node = queue.popleft()  # 从队列的左端移除节点
"""
