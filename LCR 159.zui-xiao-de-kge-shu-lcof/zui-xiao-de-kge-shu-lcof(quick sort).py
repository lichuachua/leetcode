class Solution:
    def quicksort(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[len(arr) // 2]
            left, midle, right = [], [], []
            for num in arr:
                if num < pivot:
                    left.append(num)
                elif num > pivot:
                    right.append(num)
                else:
                    midle.append(num)
        return self.quicksort(left) + midle + self.quicksort(right)

    def inventoryManagement(self, stock: List[int], cnt: int) -> List[int]:
        return self.quicksort(stock)[:cnt]


"""
Solution：先进行快速排序，再选择最小的cnt个元素
quick sort
1.选择列表的中间元素作为枢纽
2.根据枢纽对列表进行for循环选择左右区间
"""
