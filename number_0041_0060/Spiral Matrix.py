class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        col_left = 0
        col_right = len(matrix[0]) - 1

        row_up = 0
        row_down = len(matrix) - 1
        results = []
        while col_left <= col_right and row_up <= row_down:

            for index in range(col_left, col_right + 1):
                results.append(matrix[row_up][index])
            for index in range(row_up + 1, row_down + 1):
                results.append(matrix[index][col_right])
            if row_up < row_down:
                for index in range(col_right - 1, col_left - 1, -1):
                    results.append(matrix[row_down][index])
            if col_left < col_right:
                for index in range(row_down - 1, row_up, -1):
                    results.append(matrix[index][col_left])

            col_left += 1
            col_right -= 1
            row_up += 1
            row_down -= 1
        return results

