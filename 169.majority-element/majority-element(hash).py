class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = {}
        for num in nums:
            if num not in m:
                m[num] = 1
            else:
                m[num] += 1
        for key in m:
            if m[key] > len(nums) // 2:
                return key
        return 0


"""
Solution:哈希表
遍历保存出现的各元素的个数
遍历hash表，找出多数元素
"""
