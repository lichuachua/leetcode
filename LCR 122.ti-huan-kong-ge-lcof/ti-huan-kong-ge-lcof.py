class Solution:
    def pathEncryption(self, path: str) -> str:
        l = list(path)
        for i in range(len(path)):
            if l[i] == '.':
                l[i] = ' '
        return ''.join(l)
