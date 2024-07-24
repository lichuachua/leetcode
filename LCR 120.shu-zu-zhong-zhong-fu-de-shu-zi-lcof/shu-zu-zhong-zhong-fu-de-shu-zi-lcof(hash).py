class Solution:
    def findRepeatDocument(self, documents: List[int]) -> int:
        m = {}
        for i in range(len(documents)):
            if documents[i] in m:
                return documents[i]
            m[documents[i]] = 1
        return 0


"""
Solution：哈希表
同442
遍历元素存储到哈希表中，每次添加元素，查看map中是否已经存在
"""
