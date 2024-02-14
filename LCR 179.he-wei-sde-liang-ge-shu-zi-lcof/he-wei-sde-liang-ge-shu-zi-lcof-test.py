from typing import List


class Solution:
    def twoSum(self, price: List[int], target: int) -> List[int]:
        left, right = 0, len(price) - 1
        while left < right:
            if price[left] + price[right] == target:
                return [price[left], price[right]]
            elif price[left] + price[right] < target:
                left += 1
            else:
                right -= 1
        return []


re = Solution()

print(re.twoSum([3, 9, 12, 15], 18))
