class Solution:
    def reverseWords(self, s: str) -> str:
        words = self.splitWords(s)
        left, right = 0, len(words) - 1
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1
        return " ".join(words)

    def splitWords(self, s: str) -> str:
        words = []
        word = ""
        for i in range(len(s)):
            if s[i] == ' ':
                if word != "":
                    words.append(word)
                    word = ""
            else:
                word += s[i]
        if word:
            words.append(word)
        return words


"""
Solution：对撞指针
同344题
使用空格把字符串切分为单词，之后对每一个单词进行反转，
反转使用对撞指针，从0, len(s) - 1开始往中间靠拢，相互交换
"""
