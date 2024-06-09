class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0
        for num in nums:
            if count == 0:
                res = num
            if num != res:
                count -= 1
            else:
                count += 1
        return res


"""
Solution:摩尔投票法
使用result作为出现最多次的元素，count为其目前净累计[++和--]出现的次数，
result出现一次count++，非result出现一次count--，
当count==0时候，将result重新赋值给当前元素。
"""
