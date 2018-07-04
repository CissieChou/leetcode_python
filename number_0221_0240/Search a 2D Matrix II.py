class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        total_row = len(matrix)
        if total_row == 0:
            return False
        total_col = len(matrix[0])
        if total_col == 0:
            return False

        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        row = 0
        col = total_col - 1

        while row < total_row and col >= 0:
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                col -= 1
            else:
                row += 1

        return False

