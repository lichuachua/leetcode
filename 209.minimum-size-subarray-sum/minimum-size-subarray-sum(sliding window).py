class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = n + 1
        left, right = 0, 0
        window_sum = 0
        while right < n:
            window_sum += nums[right]
            while window_sum >= target:
                ans = min(ans, right - left + 1)
                window_sum -= nums[left]
                left += 1
            right += 1
        return 0 if ans == n + 1 else ans


"""
Solution:滑动窗口，双指针
用滑动窗口来记录连续子数组的和，设定两个指针：left、right，分别指向滑动窗口的左右边界，保证窗口中的和刚好大于等于target。
一开始，left、right 都指向 0。 向右移动 right，将最右侧元素加入当前窗口和 window_sum 中。
如果 window_sum ≥ target，则不断右移left，缩小滑动窗口长度，并更新窗口和的最小值，直到 window_sum<target。
然后继续右移right，直到right ≥ len(nums) 结束。
输出窗口和的最小值作为答案。

"""
