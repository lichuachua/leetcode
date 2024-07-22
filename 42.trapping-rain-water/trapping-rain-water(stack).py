class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0  # 初始化接到的雨水总量
        stack = []  # 初始化单调栈，用于存储柱子的索引
        size = len(height)  # 获取柱子高度列表的长度

        # 遍历柱子高度列表
        for i in range(size):
            # 当栈不为空且当前柱子高度大于栈顶柱子高度时，处理凹槽
            while stack and height[i] > height[stack[-1]]:
                cur = stack.pop()  # 弹出栈顶元素，获取其索引

                # 如果栈不为空，说明弹出栈顶元素后仍有左侧柱子，可以接住雨水
                if stack:
                    left = stack[-1] + 1  # 获取左侧柱子的右边界索引
                    right = i - 1  # 获取当前柱子的左边界索引
                    # 计算能接住雨水的高度
                    high = min(height[i], height[stack[-1]]) - height[cur]
                    # 更新接到的雨水总量
                    ans += high * (right - left + 1)
                else:
                    # 如果栈为空，说明左侧没有柱子，无法形成凹槽，跳出循环
                    break

            # 将当前柱子的索引压入栈中
            stack.append(i)

        return ans  # 返回接到的雨水总量


"""
Solution:栈
单调栈方法利用栈来跟踪柱子的索引，
遍历柱子列表
    对于每个柱子，循环遍历当前柱子高度和栈顶柱子高度
        如果当前柱子高度大于栈顶柱子的高度，说明可以接住雨水，弹出当前栈顶元素，计算凹槽容量
    将当前柱子的索引压入栈中

详细操作见注释
"""
