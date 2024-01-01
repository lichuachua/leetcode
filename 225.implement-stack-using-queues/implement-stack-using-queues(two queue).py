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
