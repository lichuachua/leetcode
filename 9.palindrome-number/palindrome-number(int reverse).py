class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        y = x
        res = 0
        while x != 0:
            res = res * 10 + x % 10
            x = x // 10
        if y == res:
            return True
        else:
            return False
