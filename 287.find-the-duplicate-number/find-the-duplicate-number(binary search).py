class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 1, len(nums)
        res = -1
        while left <= right:
            mid = (left + right) // 2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count <= mid:
                left = mid + 1
            else:
                right = mid - 1
                res = mid
        return res


'''
Solution: 二分法搜索
元素值二分，重复数落在 [1, n] ，可以对 [1, n] 这个值域二分查找。
mid = (1+ n) / 2，重复数要么落在[1, mid]，要么落在[mid + 1, n]。
遍历原数组，统计 <= mid 的元素个数，记为 count。
如果count > mid，说明有超过 mid 个数落在[1, mid]，但该区间只有 mid 个“坑”，说明重复的数落在[1, mid]。
相反，如果count <= mid，则说明重复数落在[mid + 1, n]。
对重复数所在的区间继续二分，直到区间闭合，重复数就找到了。
'''
