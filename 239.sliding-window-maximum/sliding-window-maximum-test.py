import heapq
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # 注意 Python 默认的优先队列是小根堆
        # 初始化一个堆q，它包含前k个元素的负值和对应的索引。
        # 由于我们使用了小顶堆，所以取负值是为了使堆顶的元素实际上是原数组中的最大值。
        q = [(-nums[i], i) for i in range(k)]
        # 将列表q转换为堆
        heapq.heapify(q)
        # 将第一个滑动窗口的最大值（即堆顶元素的负值的相反数）添加到结果列表res中。
        res = [-q[0][0]]

        for i in range(k,n):
            # 将当前元素的负值和索引推入堆中。
            heapq.heappush(q, (-nums[i], i))
            # 该元素已经不在当前的滑动窗口内了
            while q[0][1]<=i-k:
                # 从堆中移除。
                heapq.heappop(q)
            # 将当前滑动窗口的最大值（即堆顶元素的负值的相反数）添加到结果列表res中。
            res.append(-q[0][0])
        return res



re = Solution()
print(re.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
