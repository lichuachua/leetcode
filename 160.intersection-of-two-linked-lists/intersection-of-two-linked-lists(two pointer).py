# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        '''
        使用双指针a和b，a先遍历headA再遍历headB，
        b先遍历headB再遍历headA，这样的话，
        a和b所遍历的长度都是m+n，
        当a，b分别在第二次经过相交节点的时候，肯定会会相遇
        '''
        a, b = headA, headB
        while a != b:
            if a is None:
                a = headB
            else:
                a = a.next
            if b is None:
                b = headA
            else:
                b = b.next
        return a


"""
Solution: 双指针
使用双指针a和b，a先遍历headA再遍历headB，
b先遍历headB再遍历headA，这样的话，
a和b所遍历的长度都是m+n，
当a，b分别在第二次经过相交节点的时候，肯定会会相遇
"""
