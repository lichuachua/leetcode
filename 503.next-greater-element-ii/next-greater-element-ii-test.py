from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        stack = []
        for i in range(n * 2):
            while stack and nums[i % n] > nums[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = nums[i % n]
            stack.append(i % n)
        return ans



re = Solution()
print(re.nextGreaterElements([1,2,3,4,3]))
