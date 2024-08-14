# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        queue = [root]
        end = False  # 标记是否遇到空节点

        while len(queue) > 0:
            node = queue.pop(0)  # 从队列的开头移除节点

            if node is not None:
                if end:
                    return False
                queue.append(node.left)
                queue.append(node.right)
            else:
                end = True  # 遇到空节点后，标记后续节点必须为 None

        return True


"""
Solution：迭代
使用队列迭代树

1. **队列初始化**：
   - 使用 `deque` 来模拟队列，并将根节点加入队列。

2. **层次遍历**：
   - 遍历队列中的每个节点，遇到非 `None` 节点时将其子节点加入队列。
   - 遇到 `None` 节点后，标记 `end` 为 `True`，意味着后续所有节点都必须是 `None`。

3. **验证完全性**：
   - 如果在 `end` 标记后还遇到非空节点，则说明树不完整。



其中        queue = [root]和            node = queue.pop(0)
可以换为        queue = deque([root])  # 使用 deque 作为队列     和            node = queue.popleft()  # 从队列的左端移除节点
"""
