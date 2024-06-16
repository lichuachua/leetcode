class Solution:
    # 计算从数字1到数字n（包含）总共有多少位数字
    def count_num(self, n: int):
        if n < 10:
            return n
        m = len(str(n))
        # 从10^(m-1)到n（包含）的数字个数。乘以m后，表示这些数字总共有多少位。
        # 计算从1到10^(m-1)-1的数字的总位数。
        return (n - 10 ** (m - 1) + 1) * m + self.count_num(10 ** (m - 1) - 1)

    def findNthDigit(self, n: int) -> int:
        # 从1到n的数字的总位数
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            # 如果从1到mid的数字总位数大于n，说明第n个数字在mid的左侧，因此更新右边界right = mid。
            if self.count_num(mid) > n:
                right = mid
            # 如果从1到mid的数字总位数小于n，说明第n个数字在mid的右侧，因此更新左边界left = mid + 1。
            elif self.count_num(mid) < n:
                left = mid + 1
            # 如果从1到mid的数字总位数等于n，理论上说，此时mid应该是我们要找的数字
            else:
                return int(str(mid)[-1])
        # 通过计算(n - count_num(right - 1))来确定第n个数字在right中的位置，并返回该位数字
        return int(str(right)[n - self.count_num(right - 1) - 1])


re = Solution()
print(re.count_num(11))
print(re.findNthDigit(13))
