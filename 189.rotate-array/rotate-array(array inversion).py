class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)  # 将 k 取模，防止 k 大于数组长度
        nums[:] = nums[::-1]
        nums[:] = nums[:k][::-1] + nums[k:][::-1]
