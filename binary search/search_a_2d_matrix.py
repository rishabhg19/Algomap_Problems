class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        while top <= bottom:
            midrow = (top + bottom) // 2
            if target == matrix[midrow][0]:
                return True
            if target < matrix[midrow][0]:
                bottom = midrow - 1
            else:
                top = midrow + 1
        searchRow = matrix[bottom]
        print(searchRow, target)
        left = 0
        right = len(searchRow) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == searchRow[mid]:
                return True
            if target < searchRow[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return False