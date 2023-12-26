class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        ge = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        shi = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        bai = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        qian = ["", "M", "MM", "MMM"]
        res = qian[num // 1000] + bai[num % 1000 // 100] + shi[num % 100 // 10] + ge[num % 10]
        return res
