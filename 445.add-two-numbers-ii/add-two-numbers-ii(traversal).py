# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        res = None
        jinwei = 0
        while stack1 or stack2 or jinwei != 0:
            num1 = stack1.pop() if stack1 else 0
            num2 = stack2.pop() if stack2 else 0
            sum_num = num1 + num2 + jinwei
            jinwei = sum_num // 10
            sum_num %= 10
            cur_node = ListNode(sum_num)
            cur_node.next = res
            res = cur_node
        return res


"""
Solution：遍历，栈的思想
类似题 2
遍历链表转存在2个数组(栈)中
取出栈顶元素进行相加，放在链表中
"""
