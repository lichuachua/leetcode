class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            # 如果当前元素与前一个元素相同，则跳过
            while i < len(nums1) - 1 and nums1[i] == nums1[i + 1]:
                i += 1

            while j < len(nums2) - 1 and nums2[j] == nums2[j + 1]:
                j += 1
            # 比较当前元素
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return res


"""
Solution:双指针
1.先对2个list进行排序
2.i和j都从两个数组的0开始，遍历数组
    先排除两个数组中各自重复的元素
    再比较两个数组中元素的值
        相等则放到res
        nums1的元素小，i++
        nums2的元素小，j++



"""
