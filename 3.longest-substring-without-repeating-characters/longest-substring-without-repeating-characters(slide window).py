class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        windorw = dict()
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


"""
Solution：滑动窗口
用滑动窗口 window 来记录不重复的字符个数，window 为哈希表类型。 
设定两个指针：left、right，分别指向滑动窗口的左右边界，保证窗口中没有重复字符。 
一开始， left、 right 都指向 0。 向右移动right，将最右侧字符s[right] 加入当前窗口window 中，记录该字符个数。 
如果该窗口中该字符的个数多于 1 个，即window[s[right]]>1，滑动窗口内有重复的元素，则不断右移left，left++去删除重复元素，缩小滑动窗口长度，并更新窗口中对应字符的个数。直到window[s[right]]≤1。 
维护更新无重复字符的最长子串长度。然后继续右移right，直到 right≥len(nums) 结束。 
输出无重复字符的最长子串长度。
"""
