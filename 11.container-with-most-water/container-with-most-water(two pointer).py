class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        res = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            res = max(area, res)
            # 小的那条边进行移动
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res


"""
Solution：双指针
容纳的水量是由 左右两端直线中较低直线的高度 * 两端直线之间的距离 所决定的。所以我们应该使得 较低直线的高度尽可能的高，这样才能使盛水面积尽可能的大。
移动较低直线所在的指针位置，从而得到不同的高度和面积，最终获取其中最大的面积。
具体做法如下： 使用两个指针 left，right。left 指向数组开始位置，right 指向数组结束位置。
计算 left 和 right 所构成的面积值，同时维护更新最大面积值。
判断 left 和 right 的高度值大小。
如果 left 指向的直线高度比较低，则将 left 指针右移。
如果 right 指向的直线高度比较低，则将 right 指针左移。
如果遇到 left == right，跳出循环，最后返回最大的面积。
"""
