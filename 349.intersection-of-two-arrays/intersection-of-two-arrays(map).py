class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        m = {}
        for i in range(len(nums1) - 1):
            m[nums1[i]] = 1
        for i in range(len(nums2) - 1):
            if nums2[i] in m and m[nums2[i]] == 1:
                res.append(nums2[i])
                m[nums2[i]] = 0
        return res
