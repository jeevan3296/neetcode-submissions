class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        t = 0
        b = rows - 1
        while t <= b:
            mid = (t + ((b-t)//2))
            if target > matrix[mid][-1]:
                t = mid+1
            elif target < matrix[mid][0]:
                b = mid-1
            else:
                break
        else:
            return False

        row = matrix[mid]
        l = 0
        r = len(row)-1
        while l<=r:
            m = l + ((r-l)//2)
            if row[m] == target:
                return True
            elif row[m] < target:
                l = m+1
            else:
                r = m-1
        return False
