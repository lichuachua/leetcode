class Solution:
    def __init__(self, nums: List[int]):
        self.ori = nums.copy()
        self.nums = nums

    def reset(self) -> List[int]:
        self.nums = self.ori
        return self.nums

    def shuffle(self) -> List[int]:
        self.shut = self.nums.copy()
        for i in range(len(self.shut)):
            j = random.randrange(i, len(self.shut))
            self.shut[i], self.shut[j] = self.shut[j], self.shut[i]
        return self.shut


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

"""
Solution:洗牌法
可能题意难理解
init和reset其实本质上不起作用，关键在shuffle函数。
就是给定一个不重复的数组，返回可能的所有排列组合关系。
利用洗牌规则，第一个元素可能是n个里面选择；
第二个元素可能是从剩下的n-1个元素中选择（第一个已经选出不可再使用）
"""
