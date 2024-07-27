class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for tmp in zip(*strs):
            tmp_set = set(tmp)
            if len(tmp_set) == 1:
                res += tmp[0]
            else:
                break
        return res


"""
Solution：内置函数
使用zip内置方法，将多个字符串转为纵向元组，即：strs = ["flower", "flow", "flight"]，那么 zip(*strs) 生成的结果是 ('f', 'f', 'f')，('l', 'l', 'l')，('o', 'o', 'i') 
将元组转为set（去重）
去重后长度为1，则元素相同
"""
