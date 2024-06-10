class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res = res ^ nums[i]
        return res


"""
Solution:位运算
    异或运算 ⊕ 的三个性质：任何数和 0 做异或运算，结果仍然是原来的数，即a⊕0=a。 
    数和其自身做异或运算，结果是 0，即a⊕a=0。 
    异或运算满足交换率和结合律：a⊕b⊕a=b⊕a⊕a=b⊕(a⊕a)=b⊕0=b。
"""
