class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        m = {}
        for i in range(len(nums1) - 1):
            m[nums1[i]] = 1
        for i in range(len(nums2) - 1):
            if nums2[i] in m and m[nums2[i]] == 1:
                res.append(nums2[i])
                # 避免重复
                m[nums2[i]] = 0
        return res


"""
Solution:哈希表
使用一个hash map存储nums1中的元素（出现就标记为1）
遍历nums2，如果hash map中存在nums2中的元素，则将其添加到结果res中。并且置hash map中的nums2元素为0，防止重复
"""
