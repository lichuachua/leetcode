from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = {}
        res = []
        for item in nums1:
            if item in m:
                m[item] += 1
            else:
                m[item] = 1
        for item in nums2:
            if item in m and m[item] > 0:
                res.append(item)
                m[item] -= 1
        return res


re = Solution()
print(re.intersect([1, 2, 3], [1, 2, 3]))
