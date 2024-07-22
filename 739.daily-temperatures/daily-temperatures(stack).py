class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)
        return ans


"""
Solution:单调递增栈
最简单的就是暴力，对于每个温度值，向后依次进行搜索，找到比当前温度更高的值。更好的方式使用「单调递增栈」

使用单调栈来解决这个问题。单调栈是一种栈数据结构，其元素保持递增或递减顺序。
初始化一个栈，这个栈用来存储索引，计算与「右侧第一个比索引下标更大的元素」。
遍历温度列表，对于每个温度：
    如果当前温度比栈顶索引对应的温度高，此时当前元素就是栈顶元素的下一个更高值，则弹出栈顶索引并计算当前索引与弹出索引的差值。
    将当前索引压入栈。
遍历完成后，栈中剩余的索引对应的位置填0，因为这些位置之后没有更高的温度。

"""
