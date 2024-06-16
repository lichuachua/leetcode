class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = left + (right - left) // 2
            midVal = matrix[mid // n][mid % n]
            if midVal < target:
                left = mid + 1
            elif midVal > target:
                right = mid - 1
            else:
                return True
        return False


"""
Solution：二分法，折半查找
每行中的整数从左到右按非严格递增顺序排列。
每行的第一个整数大于前一行的最后一个整数。
三行拼在一起得
a=[1,3,5,7,10,11,16,20,23,30,34,60]是一个有序数组
我们可以用二分查找判断 target是否在 matrix中

"""
