class Solution:
    def checkDynasty(self, places: List[int]) -> bool:
        ma, mi = 0, 14
        m = {}
        for place in places:
            # 跳过未知朝代
            if place == 0:
                continue
            # 判断是否有重复
            if place in m:
                return False
            else:
                m[place] = 1

            if place > ma:
                ma = place
            if place < mi:
                mi = place
        return ma - mi < 5


"""
Solution：哈希表

此 5 个朝代连续的 说明
除未知朝代外，所有朝代无重复；
设此 5 个朝代中最大的朝代为 ma ，最小的朝代为 mi ，则需满足：
ma−mi<5

使用哈希表存储，判断是否有重复的元素，0直接跳过
找到最大最小元素，查看其差值
"""
