class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        s = s.lower()
        while left <= right:
            if not (s[left].isdigit() or s[left].isalpha()):
                left += 1
                continue
            if not (s[right].isdigit() or s[right].isalpha()):
                right -= 1
                continue
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
        return True


"""
Solution:双指针
left和right分别从开头和结尾往中间移动进行比较，同时需要先验证其值是数字和字母

"""
