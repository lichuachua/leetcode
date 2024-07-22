class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        stack = []
        for i in range(n * 2):
            while stack and nums[i % n] > nums[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = nums[i % n]
            stack.append(i % n)
        return ans


"""
Solution:单调递增栈
类似739，区别在于，对于每个元素，找到其下一个更大元素。如果不存在，返回-1。数组是循环的，所以需要遍历数组两次，只保留前半部分的值。

使用单调栈来解决这个问题。单调栈是一种栈数据结构，其元素保持递增或递减顺序。
初始化一个栈，这个栈用来存储索引，计算与「右侧第一个比索引下标更大的元素」。
遍历 列表，对于每个 值：
    如果当前 值比栈顶索引对应的 值高，此时当前元素就是栈顶元素的下一个更高值，则弹出栈顶索引并计算当前索引与弹出索引的差值。
    将当前索引压入栈。
遍历完成后，栈中剩余的索引对应的位置填0，因为这些位置之后没有更高的 值。

"""
