class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if matrix[0] is None or matrix is None:
            return False

        cols = len(matrix[0])
        rows = len(matrix)
        l = 0
        r = cols * rows - 1

        while l <= r:
            mid = l + (r - l)//2
            midRow = mid//cols 
            midCol = mid % cols

            if matrix[midRow][midCol] < target:
                l = mid + 1
            elif matrix[midRow][midCol] > target:
                r = mid - 1
            else:
                return True
        return False


