class Solution:
    def twoSum(self, price: List[int], target: int) -> List[int]:
        m = {}
        for index in range(len(price)):
            if target - price[index] in m:
                return target - price[index], price[index]
            else:
                m[price[index]] = index
