class Solution:
    def quick_select(self, arr: List[int], cnt: int) -> List[int]:
        if len(arr) <= 1:
            return arr

        pivot = arr[len(arr) // 2]
        left, middle, right = [], [], []

        for num in arr:
            if num < pivot:
                left.append(num)
            elif num > pivot:
                right.append(num)
            else:
                middle.append(num)

        if cnt <= len(left):
            # 小于 cnt 的元素全部在 left 中，递归划分
            return self.quick_select(left, cnt)
        elif cnt > len(left) + len(middle):
            # 小于 cnt 的元素部分在 right 中，递归划分
            return left + middle + self.quick_select(right, cnt - len(left) - len(middle))
        else:
            # 小于 cnt 的元素在 left 和 middle 中
            return left + middle[:cnt - len(left)]

    def inventoryManagement(self, stock: List[int], cnt: int) -> List[int]:
        return self.quick_select(stock, cnt)


"""
Solution：使用快速选择
相比快速排序，这个好处是在排序过程中就选择最小的cnt个值，节省后面元素排序的过程
"""
