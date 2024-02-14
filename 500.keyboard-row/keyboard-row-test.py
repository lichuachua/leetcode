from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        m = {}
        m["q"] = 1
        m["w"] = 1
        m["e"] = 1
        m["r"] = 1
        m["t"] = 1
        m["y"] = 1
        m["u"] = 1
        m["i"] = 1
        m["o"] = 1
        m["p"] = 1
        m["a"] = 2
        m["s"] = 2
        m["d"] = 2
        m["f"] = 2
        m["g"] = 2
        m["h"] = 2
        m["j"] = 2
        m["k"] = 2
        m["l"] = 2
        m["z"] = 3
        m["x"] = 3
        m["c"] = 3
        m["v"] = 3
        m["b"] = 3
        m["n"] = 3
        m["m"] = 3
        res = []
        for i in range(len(words)):
            flag = 0
            w = words[i].lower()
            for j in range(len(w) - 1):
                if m[w[j]] != m[w[j + 1]]:
                    flag = 1
                    break
            if flag == 0:
                res.append(words[i])

        return res


re = Solution()
print(re.findWords(["Hello", "Alaska", "Dad", "Peace"]))
