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
