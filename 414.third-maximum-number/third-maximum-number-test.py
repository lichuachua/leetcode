from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        min_int = float('-inf')
        a,b,c = min_int,min_int,min_int
        for num in nums :
            if num > a :
                a,b,c = num,a,b
            elif num > b :
                if num == a:
                    continue
                b,c = num,b
            elif num > c :
                if num == b:
                    continue
                c = num
        return a if c == min_int else c

re = Solution()
result = re.thirdMax([2,2,3,1])
print(result)
