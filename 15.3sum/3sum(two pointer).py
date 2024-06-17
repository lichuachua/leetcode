class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n):
            # 去除i的重复元素(要求返回不重复的三元组)
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                # 去除left的重复元素(要求返回不重复的三元组)
                while left < right and left > i + 1 and nums[left] == nums[left - 1]:
                    left += 1
                # 去除right的重复元素(要求返回不重复的三元组)
                while left < right and right < n - 1 and nums[right] == nums[right + 1]:
                    right -= 1
                if left < right and nums[i] + nums[left] + nums[right] == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        return ans


"""
题意：判断 nums 中是否存在三个元素 a、 b、 c，满足 a+b+c==0，不重复的三元组
    （题目中的“i != j、i != k 且 j != k”说的是三个数的下标不同）。
解法：先将数组进行排序，以保证按顺序查找 a、 b、 c 时，元素值为升序，从而保证所找到的三个元素是不重复的。
第一重循环遍历 a，对于每个 a 元素，从 a 元素的下一个位置开始，使用对撞指针 left，right。
left 指向 a 元素的下一个位置，  right 指向末尾位置。
先将left 右移、 right 左移去除重复元素(要求返回不重复的三元组)，再进行下边的判断。
如果nums[a]+nums[left]+nums[right]==0，则得到一个解，将其加入答案数组中，并继续将 left 右移，right 左移；
如果nums[a]+nums[left]+nums[right]>0，说明 nums[right] 值太大，将 right 向左移；
如果nums[a]+nums[left]+nums[right]<0，说明 nums[left] 值太小，将 left 右移。
"""
