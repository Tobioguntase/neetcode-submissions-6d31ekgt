class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0 
        high = len(matrix) - 1
        r = 0
        while low <= high:
            mid = (low + high) // 2


            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                r = mid
                break
            elif target < matrix[mid][0]:
                high = mid - 1
            elif target > matrix[mid][-1]:
                low = mid + 1
            else:
                return False

        low = 0 
        high = len(matrix[0]) - 1

        while low <= high:
            mid = (low + high) // 2


            if target == matrix[r][mid]:
                return True
            elif target < matrix[r][mid]:
                high = mid - 1
            elif target > matrix[r][mid]:
                low = mid + 1
            else:
                return False
        return False

        