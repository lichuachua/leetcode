class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(2, n):
            left, right = 0, i - 1
            while left < right:
                if nums[left] + nums[right] <= nums[i]:
                    left += 1
                else:
                    ans += (right - left)
                    right -= 1
        return ans


"""
Solution：双指针
三角形任意两边和大于第三边，如果我们将三条边升序排序，假设a≤b≤c，则如果满足 a+b>c，则 a+c>b 和 b+c>a 一定成立。
所以说可以使用下面的方案解决：
对数组从小到大排序，使用 ans 记录三元组个数。
从 i=2 开始遍历数组的每一条边，i 作为最大边。
使用双指针left、right。left 指向 0，right 指向 i−1。保证三条边的序号关系为：left<right<i

如果 nums[left]+nums[right]≤nums[i]，说明第一条边太短了，可以增加第一条边长度，所以将 left 右移，即 left += 1。
如果 nums[left]+nums[right]>nums[i]，说明可以构成三角形，并且第二条边固定为 right 边的话，第一条边可以在[left,right−1] 中任意选择。
所以三元组个数要加上 right−left，即 ans += (right - left)。之后将 right 左移，即 right -= 1，重新统计。
直到 left==right 跳出循环，输出三元组个数 ans。
"""
