class Solution:
    def judge(self, pattern: List[str], words: List[str]) -> bool:
        m = {}
        if len(pattern)!= len(words):
            return False
        for i in range(len(pattern)) :
            if pattern[i] in m :
                if m[pattern[i]] != words[i]:
                    return False
            else:
                m[pattern[i]] = words[i]
        return True

    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern = list(pattern)
        words = s.split()
        return self.judge(pattern,words) & self.judge(words,pattern)