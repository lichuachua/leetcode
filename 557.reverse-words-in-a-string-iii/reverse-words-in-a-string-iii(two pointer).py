class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
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
