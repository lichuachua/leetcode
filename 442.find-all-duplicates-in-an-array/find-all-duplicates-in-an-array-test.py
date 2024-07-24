from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                res.append(abs(nums[i]))
            else:
                nums[index] = -nums[index]
        return res

"""
Solution：置负
遍历数组，将元素值 对应下标的元素 置为负，
后续遍历如果发现【元素值 对应下标的元素】为负，则说明重复
"""

re = Solution()
print(re.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
