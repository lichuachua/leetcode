# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        a = []
        while head:
            a.append(head.val)
            head = head.next
        i, j = 0, len(a) - 1
        while i <= j:
            if a[i] != a[j]:
                return False
            i += 1
            j -= 1
        return True


"""
Solution:遍历+双指针
利用数组，将链表元素依次存入。
然后再使用两个指针，一个指向数组开始位置，一个指向数组结束位置。
依次判断首尾对应元素是否相等，如果都相等，则为回文链表。如果不相等，则不是回文链表。
"""
