class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        m1, m2 = [0] * 26, [0] * 26
        for i in range(len(s)):
            m1[ord(s[i]) - ord('a')] += 1
            m2[ord(t[i]) - ord('a')] += 1
        return m1 == m2


"""
Solution：遍历+数组
使用2个长度为26的数组保存字符串元素个数，直接比较数组是否相等
"""
