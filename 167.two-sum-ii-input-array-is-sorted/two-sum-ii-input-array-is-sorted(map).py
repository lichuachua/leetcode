class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        m = {}
        for index in range(len(numbers)):
            if target - numbers[index] in m:
                return m[target - numbers[index]] + 1, index + 1
            else:
                m[numbers[index]] = index
