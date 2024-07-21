class Solution:
    def calculate(self, s):
        stack = []
        pre_op = '+'
        num = 0
        for i, each in enumerate(s):
            if each.isdigit():
                num = 10 * num + int(each)
            if i == len(s) - 1 or each in '+-*/':
                if pre_op == '+':
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-num)
                elif pre_op == '*':
                    stack.append(stack.pop() * num)
                elif pre_op == '/':
                    top = stack.pop()
                    if top < 0:
                        stack.append(int(top / num))
                    else:
                        stack.append(top // num)
                pre_op = each
                num = 0
        return sum(stack)


"""
Solution:栈模拟
类似224，区别在于有'*', '/'，而没有括号
使用栈模拟出现 数字、运算符 字符时候的操作
注意：
    在Python中，// 运算符表示地板除（floor division），它总是向下取整，即向负无穷方向取整。这种行为对于正数和负数是不同的：
    对于正数，a // b 等同于 int(a / b)，结果向下取整。
    对于负数，a // b 也向下取整，这意味着它会比实际的商小。
So：
当符号是'/'时候
    当 top 是负数时，直接使用 int(top / num) 可以得到向零取整的结果。
    当 top 是非负数时，top // num 就能直接得到正确的结果，因为它本身就是向零取整。
"""
