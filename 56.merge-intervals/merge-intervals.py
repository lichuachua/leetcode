class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        for interval in intervals:
            if not res:
                res.append(interval)
            elif res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res


"""
Solution: 排序
首先根据区间的起点做了一个升序排序；
其次根据前一个区间的终点和后一个区间的起点是否有重合，判断区间是否可以合并；
最后，合并后的区间起点一定是靠前的那个区间的起点，终点是两个区间中终点更大的那个；

"""
