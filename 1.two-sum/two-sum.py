class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for index in range(len(nums)):
            if target - nums[index] in m:
                return m[target - nums[index]], index
            else:
                m[nums[index]] = index


"""
Solution: 哈希表
遍历数组，判断target-元素的值是否在map中，
    如果在，则返回map的val（index）
    否则，元素保存在map中
"""
