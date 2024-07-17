# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        res = ListNode(0, head)
        tmp = res
        while tmp.next is not None and tmp.next.next is not None:
            if tmp.next.val == tmp.next.next.val:
                duplicatesNum = tmp.next.val
                while tmp.next is not None and tmp.next.val == duplicatesNum:
                    tmp.next = tmp.next.next
            else:
                tmp = tmp.next
        return res.next


"""
Solution:双指针遍历
需要先设置一个哑点，因为第一个元素也可能需要删除。
两个指针指向当前元素和下一个元素，如果相等则标记重复元素为当前元素，比较之后的所有元素，删除与duplicatesNum相等的元素
"""
