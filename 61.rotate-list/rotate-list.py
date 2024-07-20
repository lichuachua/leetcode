# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 0:
            return head
        tmp = head
        count = 1
        while head.next is not None:
            head = head.next
            count += 1
        head.next = tmp
        i = 1
        k %= count
        while i < count - k:
            tmp = tmp.next
            i += 1
        result = tmp.next
        tmp.next = None
        return result


"""
Solution:
先将链表先连成环，然后将链表在指定位置断开。
复制头节点地址
先遍历一遍，求出链表节点个数 n，并且将最后的元素链接到头节点（连成环）。
    注意到 k 可能很大，我们只需将链表右移 k % n 个位置即可。
第二次遍历到 n - k % n 的位置，记录应该断开后新链表头节点位置，再将其断开并返回新的头节点。
"""
