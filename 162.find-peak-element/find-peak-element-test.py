from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 判断峰值
        isUp = True
        isDone = True
        for i in range(1, len(nums) - 1):
            if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
                return i
            elif nums[i - 1] < nums[i]:
                isDone = False
            elif nums[i - 1] > nums[i]:
                isUp = False
        # 特殊判断————升序或者降序，上面的逻辑行不通
        if isUp:
            return len(nums) - 1
        if isDone:
            return 0
        return 0


re = Solution()
print(re.findPeakElement([3, 2, 1]))
