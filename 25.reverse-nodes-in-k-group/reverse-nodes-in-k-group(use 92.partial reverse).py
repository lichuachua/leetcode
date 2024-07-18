# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        start = prev.next
        then = start.next

        for _ in range(right - left):
            start.next = then.next
            then.next = prev.next
            prev.next = then
            then = start.next

        return dummy.next

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        count = 0

        # Count the number of nodes in the list
        while current.next:
            current = current.next
            count += 1

        prev = dummy

        while count >= k:
            start = prev.next
            # 因为从0开始算的
            end = prev
            for _ in range(k):
                end = end.next

            next_start = end.next
            end.next = None  # Temporarily break the chain

            # Reverse the sublist
            reversed_list = self.reverseBetween(start, 1, k)

            # Connect the reversed sublist back to the main list
            prev.next = reversed_list

            start.next = next_start
            prev = start

            count -= k

        return dummy.next


"""
Solution:遍历迭代的思想
链表反转为206，部分反转为92，此题目是进行多次部分反转
本题中，我们可以以 k 为单位对链表进行切分，然后分别对每个区间部分进行反转。最后再返回头节点即可。
但是需要注意一点，如果需要反转的区间包含了链表的第一个节点，那么我们可以事先创建一个哑节点作为链表初始位置开始遍历，这样就能避免找不到需要反转的链表区间的前一个节点。

1.遍历链表并统计节点总数，
2.使用 reverseBetween 方法按组进行翻转。
3.对于每组长度为 k 的部分进行反转，如果剩余部分不足 k 则保持原样。
"""
