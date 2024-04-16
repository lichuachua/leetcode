# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        '''
        两个链表长度不一样，定不下来在倒数第几个元素相交 ，
        能想到的就是找到两个链表中短的那个，
        并且将长链表按照短链表长度将其头部多余节点去掉，
        之后遍历长度一样的链表就和完一样了
        '''
        countA, countB = 0, 0
        a, b = headA, headB
        while a:
            countA += 1
            a = a.next
        while b:
            countB += 1
            b = b.next
        if countA > countB:
            differ = countA - countB
            while differ > 0:
                headA = headA.next
                differ -= 1
        else:
            differ = countB - countA
            while differ > 0:
                headB = headB.next
                differ -= 1
        while headA and headB:
            if headA == headB:
                return headA
            headA, headB = headA.next, headB.next
        return None
