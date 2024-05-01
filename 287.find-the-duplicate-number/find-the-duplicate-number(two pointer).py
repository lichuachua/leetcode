class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 快慢指针：类似判断链表是否有环的题解
        # 将这些数字想象成链表中的结点，数组中数字代表下一个结点的数组下标
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow, fast = nums[slow], nums[nums[fast]]
        # 目前slow和fast相等，重置slow的值，找到重复的值
        slow = 0
        while slow != fast:
            slow, fast = nums[slow], nums[fast]
        return slow
