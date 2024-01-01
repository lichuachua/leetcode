class MyQueue:

    def __init__(self):
        self.stack1 = []  # 栈1为队列
        self.stack2 = []  # 栈2为辅助队列

    def push(self, x: int) -> None:
        self.stack1.append(x)  # 在栈顶进行插入，s1栈顶为队尾

    def pop(self) -> int:
        # s2为辅助队列,将s1的元素（除了最后一个元素）从栈顶出栈，从s2栈顶入栈
        for i in range(len(self.stack1) - 1, 0, -1):
            self.stack2.append(self.stack1[i])
        res = self.stack1[0]  # 栈顶元素
        self.stack1 = []
        # 同样的操作，将栈s2的元素回到栈s1
        for i in range(len(self.stack2) - 1, -1, -1):
            self.stack1.append(self.stack2[i])
        self.stack2 = []
        return res

    def peek(self) -> int:
        # s2为辅助队列
        for i in range(len(self.stack1) - 1, 0, -1):
            self.stack2.append(self.stack1[i])
        res = self.stack1[0]  # 栈顶元素
        self.stack2 = []
        return res

    def empty(self) -> bool:
        return len(self.stack1) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
