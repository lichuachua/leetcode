# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow


"""
Solution:快慢指针
类似141
快指针走两步，慢指针走一步，若存在环，迟早快慢指针相遇，若快指针到链表末尾，则无环。
也是使用快慢指针，但需要找到相遇点后，再找到环的入口。
首先使用和0141相同的方法找到相遇点。
确定存在环后，将一个指针（slow）移回链表头，另一个指针（fast）留在相遇点。
然后两个指针每次都移动一步，它们最终会在环的入口处相遇。

这是因为：假设入环位置为 A，快慢指针在 B 点相遇，则相遇时慢指针走了 𝑎 + 𝑏 步，快指针走了 a+n(b+c)+b 步。 
因为快指针总共走的步数是慢指针走的步数的两倍，即 2(a+b)=a+n(b+c)+b，所以可以推出：a=c+(n−1)(b+c)。
 我们可以发现：从相遇点到入环点的距离 c 加上 n−1 圈的环长 b+c 刚好等于从链表头部到入环点的距离。
"""
