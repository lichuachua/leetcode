from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n):
            # 去除i的重复元素
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                # 去除left的重复元素
                while left < right and left > i + 1 and nums[left] == nums[left - 1]:
                    left += 1
                # 去除right的重复元素
                while left < right and right < n - 1 and nums[right] == nums[right + 1]:
                    right -= 1
                if left < right and nums[i] + nums[left] + nums[right] == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        return ans


re = Solution()
print(re.threeSum([-1, 0, 1, 2, -1, -4]))
