class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] < nums[right]:
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[mid] > target and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1


"""
Solution:双指针、二分法、折半查找
与 153 题属于一类
    数组经过「旋转」之后，会有两种情况，第一种就是原先的升序序列，另一种是两段升序的序列。
和正常的二分法流程是一样的，区别在于左移和右移过程不是直接比较的nums[mid]和target的大小
而是先比较nums[mid]和nums[left]，之后在比较target
"""
