class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = n + 1
        for i in range(n):
            total = 0
            for j in range(i, n):
                total += nums[j]
                if total >= target:
                    ans = min(ans, j - i + 1)
                    # 往后面肯定是越来越长，所以break
                    break
        return 0 if ans == n + 1 else ans


"""
Solution:暴力破解
Submit Result:超出时间限制
直接两层循环遍历，从每一个元素开始，到后面最近的元素满足>=target的最小值
"""
