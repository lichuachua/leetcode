class Solution:
    def findRepeatDocument(self, documents: List[int]) -> int:
        documents.sort()
        for i in range(len(documents) - 1):
            if documents[i] == documents[i + 1]:
                return documents[i]
        return documents[i]


"""
Solution：排序
同442
先对数组排序
之后遍历，相邻元素是否有相等的，相等则返回
"""
