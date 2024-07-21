from typing import List


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


re = Solution()
print(re.findDuplicate([1, 3, 4, 2, 2]))

"""
和 169 majority-element相似，只不过这个要求空间复杂度为常数级别
hash
divide and conquer
moore majority vote algorithm（需要出现超过一半才能使用）
"""
