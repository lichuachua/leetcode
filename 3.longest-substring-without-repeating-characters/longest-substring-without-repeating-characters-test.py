class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        window = dict()
        res = 0

        while right < len(s):
            # 判断right元素是否在window
            if s[right] not in window:
                window[s[right]] = 1
            else:
                window[s[right]] += 1
            # 滑动窗口内有重复的元素，left++去删除重复元素
            while window[s[right]] > 1:
                window[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res


re = Solution()
print(re.lengthOfLongestSubstring("abcabcbb"))
