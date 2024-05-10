class Solution:
    def encryptionCalculate(self, dataA: int, dataB: int) -> int:
        max = 0xffffffff
        dataA, dataB = dataA & max, dataB & max
        while dataB != 0:
            dataA, dataB = (dataA ^ dataB), (dataA & dataB) << 1 & max
        return dataA if dataA <= 0x7fffffff else ~(dataA ^ max)