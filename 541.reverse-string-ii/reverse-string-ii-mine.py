class Solution:
    # 自己的理解-稍复杂
    def myReversed(self, s: list) -> list:
        return s[::-1]
    def reverseStr(self, s: str, k: int) -> str:
        t = list(s)
        for i in range(0,len(t),k):
            if i%(2*k) == 0 :
                j = i+k
                if len(t) < j :
                    j = len(t)
                t[i:j] = self.myReversed(t[i:j])
        return "".join(t)

