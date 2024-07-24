from typing import List


class Solution:
    def checkDynasty(self, places: List[int]) -> bool:
        unknow = 0
        sorted(places)
        for i in range(4):
            if places[i] == 0:
                unknow += 1
            elif places[i] == places[i + 1]:
                return False
        return places[4] - places[unknow] < 5


re = Solution()
print(re.checkDynasty([0, 6, 9, 0, 7]))
