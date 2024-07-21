class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack = self.stack[:len(self.stack) - 1]

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        res = self.stack[len(self.stack) - 1]
        for i in range(len(self.stack) - 2, -1, -1):
            if self.stack[i] < res:
                res = self.stack[i]
        return res


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

"""
Solution:模拟
符合栈先进先出的特征进行push、pop、top。
getMin：循环遍历栈，找到最小值
其他方法：
1.栈的元素使用元组，保存当前值和栈中的最小值
2.辅助栈，保存每次存入新元素时候的栈中的最小值
"""
