class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        len1, len2 = len(num1), len(num2)
        nums = [0 for _ in range(len1 + len2)]
        for i in range(len1 - 1, -1, -1):
            digit1 = int(num1[i])
            for j in range(len2 - 1, -1, -1):
                digit2 = int(num2[j])
                nums[i + j + 1] += digit1 * digit2
        for i in range(len1 + len2 - 1, 0, -1):
            nums[i - 1] += nums[i] // 10
            nums[i] %= 10
        if nums[0] == 0:
            ans = "".join(str(digit) for digit in nums[1:])
        else:
            ans = "".join(str(digit) for digit in nums[:])
        return ans


re = Solution()
print(re.multiply("123", "456"))
