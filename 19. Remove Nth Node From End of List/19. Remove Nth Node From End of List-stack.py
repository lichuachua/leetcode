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
使用tmp = ListNode(0, head)，会出错
"""