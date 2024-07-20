# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 可能会删除第一个节点，需要设置前置节点
        res = ListNode(0, head)
        tmp = res
        stack = []
        while tmp.next is not None:
            stack.append(tmp)
            tmp = tmp.next
        prev = stack[len(stack) - n]
        prev.next = prev.next.next
        return res.next


""""tmp必须来自于res
使用tmp = ListNode(0, head)，会出错，两个地址

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 可能会删除第一个节点，需要设置前置节点
        res = ListNode(0, head)
        tmp = ListNode(0, head)
        stack1,stack2 = [],[]
        while tmp.next is not None:
            stack1.append(tmp)
            tmp = tmp.next
        while res.next is not None:
            stack2.append(res)
            res = res.next
        print(stack1)
        print()
        print(stack2)
        prev = stack1[len(stack1) - n]
        prev.next = prev.next.next
        return res.next
"""

"""
Solution: 栈（数组）
数组存储每个结点，之后找到要删除结点的前置结点，删除
"""
