class Solution:
    def inventoryManagement(self, stock: List[int], cnt: int) -> List[int]:
        stock.sort()
        return stock[:cnt]


"""
Solution:内置排序
使用内置的排序函数进行升序排序
选择前cnt个元素
"""
