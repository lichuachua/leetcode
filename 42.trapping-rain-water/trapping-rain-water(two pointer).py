class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        ans = 0
        while left < right:
            # 选择较小的一侧处理
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    # 如果当前左侧高度小于 left_max，则可以接到雨水。
                    ans += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                right -= 1
        return ans


""""
Solution：双指针
使用双指针方法，左右指针从数组两端向中间收缩，并同时维护左边最高和右边最高的高度。

具体步骤如下：
初始化左右指针 left 和 right，分别指向数组的两端。
初始化两个变量 left_max 和 right_max 来记录从左到右和从右到左的最高高度。
如果 height[left] 小于 height[right]，则移动左指针，更新 left_max 并计算能接到的雨水量。
如果 height[right] 小于等于 height[left]，则移动右指针，更新 right_max 并计算能接到的雨水量。
当左右指针相遇时，结束计算。
"""
