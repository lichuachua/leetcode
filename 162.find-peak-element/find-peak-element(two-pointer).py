class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 特殊判断长度小于3
        if len(nums) <= 1:
            return 0
        if len(nums) <= 2:
            return 0 if nums[0] > nums[1] else 1

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


"""
Solution:双指针判断
双指针判断中间元素的左右是否满足峰值，还需要处理两个特殊情况：
1. 序列长度小于3
2. 完全的升序或者降序
"""
