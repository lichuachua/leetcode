# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 可能会删除第一个节点，需要设置前置节点
        tmp = ListNode(0, head)
        fast, slow = head, tmp
        for i in range(n):
            fast = fast.next

        while fast is not None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return tmp.next


""""
Note: 在遍历时候，不能直接从头部开始遍历，要设置一个哑点作为头节点的上一个节点，因为头节点可能被删除

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 处理边界
        if head.next is None and n==1 :
            return None
        
        tmp,fast,slow = head,head,head
        i = 0 
        while i <= n :
            fast = fast.next
            i += 1
        while fast is not None :
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return tmp

"""

"""
Solution: 快慢指针
**在遍历时候，不能直接从头部开始遍历，要设置一个哑点作为头节点的上一个节点，因为头节点可能被删除**
快指针先走n步，
之后快慢指针同步没次增1
快指针到了链表尾，则慢指针为需要删除的前置结点
"""