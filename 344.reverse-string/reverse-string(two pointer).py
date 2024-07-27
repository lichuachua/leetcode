class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


"""
Solution：对撞指针
使用对撞指针，从0, len(s) - 1开始往中间靠拢，相互交换
"""
