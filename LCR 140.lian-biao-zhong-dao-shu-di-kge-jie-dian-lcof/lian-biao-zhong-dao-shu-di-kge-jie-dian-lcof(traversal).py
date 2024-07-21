# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def trainingPlan(self, head: Optional[ListNode], cnt: int) -> Optional[ListNode]:
        # 可能是第一个节点，需要设置前置节点
        res = ListNode(0, head)
        tmp = res
        stack = []
        while tmp is not None:
            stack.append(tmp)
            tmp = tmp.next
        resNode = stack[len(stack) - cnt]
        return resNode


"""
Solution: 栈（数组）
类似题目19
数组存储每个结点，之后找到要删除结点的前置结点，删除
区别：19需要删除，所以循环条件为tmp.next不为空，找前置结点，此题不需要找前置结点
"""
