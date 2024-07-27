class Solution:
    def reverseWords(self, s: str) -> str:
        s = self.splitWords(s)
        for i in range(len(s)):
            s[i] = self.reverseWord(s[i])
        return " ".join(s)

    def splitWords(self, s: str) -> List[str]:
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

    def reverseWord(self, s: str) -> str:
        s = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return "".join(s)

"""
Solution：对撞指针
类似344题
使用空格把字符串切分为单词，之后对每一个单词进行反转，
反转使用对撞指针，从0, len(s) - 1开始往中间靠拢，相互交换
"""