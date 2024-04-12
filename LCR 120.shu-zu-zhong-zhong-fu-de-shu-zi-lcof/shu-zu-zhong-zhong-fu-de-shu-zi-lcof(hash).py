class Solution:
    def findRepeatDocument(self, documents: List[int]) -> int:
        m = {}
        for i in range(len(documents)):
            if documents[i] in m:
                return documents[i]
            m[documents[i]] = 1
        return 0
