class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, count = [], "", 0
        for item in s:
            if '0' <= item <= '9':
                count = count * 10 + int(item)
            elif item == '[':
                stack.append([count, res])
                res, count = "", 0
            elif item == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            else:
                res += item
        return res

"""
Solution：栈
遍历字符串，使用栈存储【数字和结果】元组
判断字符为数字，主要是处理多位数
判断为'['，将数字和结果存储进栈，数字和结果置为空
判断为']'，取出栈中的元素进行运算的到res，
否则（为字母），res拼接字母
"""