from typing import List


class Solution:
    def findRepeatDocument(self, documents: List[int]) -> int:
        m = {}
        for i in range(len(documents)):
            if documents[i] in m:
                return documents[i]
            m[documents[i]] = 1
        return 0


re = Solution()
print(re.findRepeatDocument([2, 3, 1, 0, 2, 5, 3]))
