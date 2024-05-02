class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        '''找到范围内最大的公约数，除n看余数是否为0
        【 32 位有符号整数的范围内，3的最大幂为3^19，判断n是否能被 3^19整除】
        '''
        return n > 0 and int(math.pow(3, 19)) % n == 0
