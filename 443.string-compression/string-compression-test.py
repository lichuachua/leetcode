import copy
from typing import List


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
        print(chars)
        # 返回压缩后的新长度
        return write


re = Solution()

print(re.compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))

"""
注意，此处要求压缩原始的chars，这里更改了chars的前write个元素，后面的元素没有变，平台是使用write截断的chars，展示压缩后的chars
"""
