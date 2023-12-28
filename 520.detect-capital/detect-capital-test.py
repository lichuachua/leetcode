class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper():
            return True  # 全部字母都是大写
        elif word.islower():
            return True  # 全部字母都是小写
        elif word[0].isupper() and word[1:].islower():
            return True  # 首字母大写，其他字母小写
        else:
            return False


re = Solution()
print(re.detectCapitalUse("aDa"))
