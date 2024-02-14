class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        while i < len(nums1) - 1 and j < len(nums2) - 1:
            if nums1[i] == nums1[i + 1]:
                i += 1
                continue
            if nums2[j] == nums2[j + 1]:
                j += 1
                continue
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        if i == len(nums1) - 1:
            while j < len(nums2):
                if nums1[i] == nums2[j]:
                    res.append(nums1[i])
                    i += 1
                    j += 1
                    break
                else:
                    j += 1
        if j == len(nums2) - 1:
            while i < len(nums1):
                if nums2[j] == nums1[i]:
                    res.append(nums2[j])
                    i += 1
                    j += 1
                    break
                else:
                    i += 1
        return res
