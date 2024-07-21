class CQueue:

    def __init__(self):
        self.stack1 = []  # 栈1为队列
        self.stack2 = []  # 栈2为辅助队列

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return -1
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


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()


"""
Solution:栈
类似题目232
模拟实现，如注释
"""
