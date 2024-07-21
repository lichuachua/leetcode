class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        low, high = 0, x // 2
        while low <= high:
            mid = (low + high) // 2
            if mid * mid == x:
                return int(mid)
            elif mid * mid > x:
                high = mid - 1
            else:
                low = mid + 1
        if high * high > x:
            return int(high - 1)
        else:
            return int(high)


"""
Solution:二分查找
"""
