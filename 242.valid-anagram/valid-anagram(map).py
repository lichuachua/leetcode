class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        m = {}
        for i in s:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
        for i in t:
            if i not in m:
                return False
            m[i] -= 1
            if m[i] < 0:
                return False
        return True


"""
Solution：哈希表
比较两个字符串长度，不相等返回false
遍历字符串，将元素存储在map中，之后遍历另外一个字符串查看map中的元素
"""
