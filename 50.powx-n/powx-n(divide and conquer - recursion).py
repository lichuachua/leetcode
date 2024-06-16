class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            x = 1 / x
            n = -n
        # 当 n 为偶数时
        if n % 2 == 0:
            half = self.myPow(x, n // 2)
            return half * half

        # 当 n 为奇数时
        else:
            half = self.myPow(x, (n - 1) // 2)
            return x * half * half


"""
Solution：分治算法——递归
常规方法是直接将 x 累乘 n 次得出结果，时间复杂度为 O(n)。
我们可以利用分治算法来减少时间复杂度。
根据 n 的奇偶性，我们可以得到以下结论：
1.如果 n 为偶数：x^n=x^(n/2)*x^(n/2)
2.如果 n 为奇数：x^n=x*x^((n-1)/2)*x^((n-1)/2)
x^(n/2) 或 x^((n−1)/2) 又可以继续向下递归划分。
则我们可以利用低纬度的幂计算结果，来得到高纬度的幂计算结果。
这样递归求解，时间复杂度为 O(logn)，并且递归也可以转为递推来做。
需要注意如果 n 为负数，可以转换为 (1/x)^(-n)
"""
