class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0

        read = 0  # 用于遍历原始字符数组
        write = 0  # 用于记录压缩后的字符应该写入的位置
        count = 1  # 用于记录当前字符的连续重复次数

        while read < len(chars):
            # 遍历字符，找到不同字符组的结束位置
            while read + 1 < len(chars) and chars[read] == chars[read + 1]:
                read += 1
                count += 1

            # 将字符写入到压缩后的位置
            chars[write] = chars[read]
            write += 1

            # 如果字符重复了多次，则将长度写入到压缩后的位置
            if count > 1:
                length_str = str(count)
                for digit in length_str:
                    chars[write] = digit
                    write += 1

            # 更新read和count，开始处理下一个字符组
            read += 1
            count = 1

        # 返回压缩后的新长度
        return write


"""
Solution：双指针
使用快慢指针解决，首先使用read（快指针）用于遍历原始字符数组，write（慢指针）用于记录压缩后的字符应该写入的位置
每次从read遍历，找到当前元素重复的次数count，之后在write处添加当前元素及其次数，循环
"""
