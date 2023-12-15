class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        lcc = [2, 3, 5]
        for item in lcc:
            while n % item == 0:
                n //= item

        return n == 1