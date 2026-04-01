class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0 
        high = len(matrix) - 1

        while low <= high:
            mid = (low + high) // 2

            if target in matrix[mid]:
                return True
            elif target < matrix[mid][0]:
                high = mid - 1
            elif target > matrix[mid][-1]:
                low = mid + 1
            else:
                return False
        return False

        