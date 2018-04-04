class Solution(object):
    result = 0
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        col_indexes = [-1] * n

        self.backTrack(n, col_indexes, 0)
        return self.result

    def backTrack(self, n, col_indexes, cur_row_index):
        if cur_row_index > n:
            return
        if col_indexes == n:
            self.result += 1
            return

        for j in range(n):
            col_indexes[cur_row_index] = j
            if self.isValid(col_indexes, cur_row_index):
                self.backTrack(n, col_indexes, cur_row_index + 1)

    def isValid(self, col_indexes, cur_row_index):
        cur_col_index = col_indexes[cur_row_index]
        for k in range(cur_row_index):
            if col_indexes[k] == cur_col_index or (abs(k-cur_row_index) == abs(col_indexes[k] - cur_col_index)):
                return False
        return True
