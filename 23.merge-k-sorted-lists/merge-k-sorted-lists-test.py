# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        tmp = res
        while list1 and list2:
            if list1.val < list2.val:
                tmp.next = list1
                list1 = list1.next
            else:
                tmp.next = list2
                list2 = list2.next
            tmp = tmp.next
        if list1:
            tmp.next = list1
        else:
            tmp.next = list2
        return res.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedLists.append(self.mergeTwoLists(l1, l2))
            lists = mergedLists
        return lists[0]


l1 = ListNode(1, ListNode(4, ListNode(5)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
l3 = ListNode(2, ListNode(6))
lists = [l1, l2, l3]

re = Solution()
result = re.mergeKLists(lists)
while result:
    print(result.val)
    result = result.next
