class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = {}
        for item in magazine:
            if item in m:
                m[item] += 1
            else:
                m[item] = 1
        for item in ransomNote:
            if item in m:
                if m[item] > 0:
                    m[item] -= 1
                else:
                    return False
            else:
                return False
        return True


re = Solution()
print(re.canConstruct("aa", "aab"))
