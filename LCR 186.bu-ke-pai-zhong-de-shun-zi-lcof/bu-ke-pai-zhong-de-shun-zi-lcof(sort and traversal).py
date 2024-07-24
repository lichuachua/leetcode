class Solution:
    def checkDynasty(self, places: List[int]) -> bool:
        unknow = 0
        places.sort()  # 数组排序
        for i in range(4):
            if places[i] == 0:
                unknow += 1
            elif places[i] == places[i + 1]:
                return False
        return places[4] - places[unknow] < 5


"""
Solution：排序 + 遍历
此 5 个朝代连续的 说明
除未知朝代外，所有朝代无重复；
设此 5 个朝代中最大的朝代为 ma ，最小的朝代为 mi ，则需满足：
ma−mi<5


数组排序，找到第一个不为0的元素（最小的元素），和最后的元素（最大的元素）进行相减，差值小于5
注意：重复则直接返回false
"""
