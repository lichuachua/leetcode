class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        '''找到范围内最大的公约数，除n看余数是否为0
        【 32 位有符号整数的范围内，2的最大幂为 2^31，判断n是否能被 2^31整除】
        '''
        return n > 0 and int(math.pow(2, 31)) % n == 0
