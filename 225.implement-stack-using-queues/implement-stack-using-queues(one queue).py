class MyStack:

    def __init__(self):
        self.queue = []  # 栈

    def push(self, x: int) -> None:
        n = len(self.queue)
        self.queue.append(x)
        for _ in range(n):
            self.queue.append(self.queue[0])
            self.queue = self.queue[1:]

    def pop(self) -> int:
        res = self.queue[0]
        self.queue = self.queue[1:]
        return res

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
