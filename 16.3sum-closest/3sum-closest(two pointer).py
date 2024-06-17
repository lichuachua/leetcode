class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = float('inf')
        n = len(nums)
        for i in range(2, n):
            left, right = 0, i - 1
            while left < right:
                total = nums[left] + nums[right] + nums[i]
                if abs(total - target) < abs(ans - target):
                    ans = total
                if total < target:
                    left += 1
                else:
                    right -= 1
        return ans


"""


先对数组进行从小到大排序，使用 ans 记录最接近的三数之和。
遍历数组，对于数组元素 nums[i]，使用两个指针 left、right。
left 指向第 0 个元素位置， right 指向第 i−1 个元素位置。
计算 nums[i]、 nums[left]、 nums[right] 的和与 target 的差值，将其与 ans 与 target 的差值作比较。如果差值小，则更新ans。
如果nums[i]+nums[left]+nums[right]<target，则说明 left 小了，应该将 left 右移，继续查找。
如果nums[i]+nums[left]+nums[right]≥target，则说明 right 太大了，应该将 right 左移，然后继续判断。
当left==right 时，区间搜索完毕，继续遍历nums[i+1]。
"""
