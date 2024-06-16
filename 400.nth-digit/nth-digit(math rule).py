class Solution:
    def findNthDigit(self, n: int) -> int:
        digit = 1
        start = 1
        base = 9
        while n > base:
            n -= base
            digit += 1
            start *= 10
            base = start * digit * 9
        number = start + (n - 1) // digit
        res = (n - 1) % digit
        return int(str(number)[res])


"""
Solution：找规律
数字以 0123456789101112131415 的格式序列化到一个字符序列中。
在这个序列中，第 5 位（从下标 0 开始计数）是 5，第 13 位是 1，第 19 位是 4等。
根据题意中的字符串，找数学规律：
1 位数字有 9 个，共 9 位： 123456789。
2 位数字有 90 个，共 2×90 位： 10111213...9899。
3 位数字有 900 个，共 3×900 位： 100...999。
4 位数字有 9000 个，共4×9000 位： 1000...9999。

则我们可以按照以下步骤解决这道题：
我们可以先找到第 n 位所在整数 number 所对应的位数 digit。
同时找到该位数 digit 的起始整数 start。
再计算出 n 所在整数 number。number 等于从起始数字 start 开始的第 ⌊(n − 1 )/digit⌋ 个数字。即 number = start + (n - 1) // digit。
然后确定 n 对应的是数字  number 中的哪一位。即res = (n−1) mod digit
"""
