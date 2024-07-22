class MyStack:

    def __init__(self):
        self.queue1 = []  # 栈
        self.queue2 = []  # 中间栈

    def push(self, x: int) -> None:
        self.queue1.append(x)  # q1作为栈，插入队尾，即栈头

    def pop(self) -> int:
        for i in range(0, len(self.queue1) - 1):
            self.queue2.append(self.queue1[i])
        res = self.queue1[len(self.queue1) - 1]
        self.queue1, self.queue2 = self.queue2, []
        return res

    def top(self) -> int:
        res = self.pop()
        self.push(res)
        return res

    def empty(self) -> bool:
        return len(self.queue1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

"""
Solution：两个队列
使用辅助队列实现栈
pop 方法弹出并返回栈顶元素。
    首先，将 queue1 中除了最后一个元素之外的所有元素移动到 queue2。
    然后，保存 queue1 的最后一个元素（栈顶元素）到 res。
    接下来，交换 queue1 和 queue2，并清空 queue2。
    最后，返回栈顶元素 res。
"""
