class Solution:
    def findRepeatDocument(self, documents: List[int]) -> int:
        documents.sort()
        for i in range(len(documents) - 1):
            if documents[i] == documents[i + 1]:
                return documents[i]
        return documents[i]
