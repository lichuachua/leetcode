class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1 = len(num1) - 1
        n2 = len(num2) - 1
        jinwei = 0
        res = []
        while n1 >= 0 or n2 >= 0:
            num1_d = int(num1[n1]) if n1 >= 0 else 0
            num2_d = int(num2[n2]) if n2 >= 0 else 0
            n1 -= 1
            n2 -= 1
            # 计算结果
            num = num1_d + num2_d + jinwei
            # 存储结果
            if num > 9:
                res.append(str(num - 10))
                jinwei = 1
            else:
                res.append(str(num))
                jinwei = 0
        # 返回计算结果
        if jinwei == 1:
            res.append('1')
        return "".join(res[::-1])


re = Solution()
print(re.addStrings("456", "77"))
