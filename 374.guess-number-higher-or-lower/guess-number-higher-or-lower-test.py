# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
def guess(n):
    if n < 6:
        return 1
    elif n > 6:
        return -1
    else:
        return 0


class Solution:
    def lcc(self, low, high):
        mid = (low + high) // 2
        if guess(mid) == 0:
            return mid
        elif guess(mid) == -1:
            return self.lcc(low, mid - 1)
        else:
            return self.lcc(mid + 1, high)

    def guessNumber(self, n: int) -> int:
        return self.lcc(0, n)


re = Solution()
print(re.guessNumber(10))
