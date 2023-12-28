class Solution:
    def dismantlingAction(self, arr: str) -> str:
        m = {}
        for i in arr:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
        for i in arr:
            if m[i] == 1:
                return i
        return ' '


re = Solution()
print(re.dismantlingAction('abbcdas'))
