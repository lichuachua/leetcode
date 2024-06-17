class Solution:
    def compress(self, chars: List[str]) -> int:
        m = {}
        for char in chars:
            if char in m:
                m[char] += 1
            else:
                m[char] = 1
        write_index = 0  # 指向当前写入位置的指针
        for char, count in m.items():
            chars[write_index] = char
            write_index += 1
            if count > 1:
                count_str = str(count)
                for digit in count_str:
                    chars[write_index] = digit
                    write_index += 1

        return write_index


"""
Submit Result:执行错误，同一个字母块 出现多次 将导致失败。
输入 chars = ["a","a","a","b","b","a","a"] 输出 ["a","5","b","2"] 预期结果 ["a","3","b","2","a","2"]

Solution：使用哈希表
遍历数组，哈希表中存储key为元素，val为元素出现的次数
遍历hash，每次将key算作1位（+1），对应val的”位数“（+位数）

"""
