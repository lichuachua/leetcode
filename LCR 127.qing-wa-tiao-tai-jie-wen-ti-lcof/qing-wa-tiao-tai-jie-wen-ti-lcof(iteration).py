class Solution:
    def trainWays(self, num: int) -> int:
        if num < 2:
            return 1
        a,b = 1,2
        for i in range(3,num+1):
            a,b=b,(a+b)%1000000007
        return b