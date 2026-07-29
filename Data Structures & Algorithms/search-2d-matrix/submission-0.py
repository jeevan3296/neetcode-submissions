class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)-1

        while l <= r:
            m = (l + ((r-l)//2))
            if target in matrix[m]:
                return True
            elif target > matrix[m][-1]:
                l = m + 1
            else:
                r = m - 1
        return False

        