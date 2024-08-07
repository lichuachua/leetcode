# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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

    def mergeSort(self, head: ListNode):
        # 分割环节
        if not head or not head.next:
            return head

        # 快慢指针找到中心链节点
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # 断开左右链节点
        left_head, right_head = head, slow.next
        slow.next = None

        # 归并操作
        return self.mergeTwoLists(self.mergeSort(left_head), self.mergeSort(right_head))

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.mergeSort(head)


"""
Solution:归并排序
类似数组排序的912，、合并两个有序链表21，此题是对链表进行排序
1.分割环节：找到链表中心链节点，从中心节点将链表断开，并递归进行分割。
使用快慢指针 fast = head.next、slow = head，让 fast 每次移动 2 步，slow 移动 1 步，移动到链表末尾，从而找到链表中心链节点，即 slow。
从中心位置将链表从中心位置分为左右两个链表 left_head 和 right_head，并从中心位置将其断开，即 slow.next = None。
对左右两个链表分别进行递归分割，直到每个链表中只包含一个链节点。
2.归并环节：将递归后的链表进行两两归并，完成一遍后每个子链表长度加倍。重复进行归并操作，直到得到完整的链表。
使用哑节点 dummy_head 构造一个头节点，并使用 cur 指向 dummy_head 用于遍历。
比较两个链表头节点 left 和 right 的值大小。将较小的头节点加入到合并后的链表中。并向后移动该链表的头节点指针。
然后重复上一步操作，直到两个链表中出现链表为空的情况。
将剩余链表插入到合并中的链表中。
将哑节点 dummy_dead 的下一个链节点 dummy_head.next 作为合并后的头节点返回。

"""
