from random import randrange
from typing import List


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
            j = randrange(i, len(self.shut))
            self.shut[i], self.shut[j] = self.shut[j], self.shut[i]
        return self.shut


# Your Solution object will be instantiated and called as such:
obj = Solution([1, 2, 3])
param_1 = obj.reset()
param_2 = obj.shuffle()
print(param_1)
print(param_2)
