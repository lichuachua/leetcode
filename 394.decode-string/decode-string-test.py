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


re = Solution()
print(re.decodeString("3[a]2[bc]"))
