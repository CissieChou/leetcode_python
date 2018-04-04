class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        results = []
        col_indexes = [-1] * n
        self.backTrack(n, results, 0, col_indexes)
        return results

    def backTrack(self, n, results, cur_row_index, col_indexes):
        if cur_row_index == n:
            single_result = []
            for i in range(n):
                line = ["."] * n
                line[col_indexes[i]] = "Q"
                single_result.append("".join(line))
            results.append(single_result)
            return

        for j in range(n):
            col_indexes[cur_row_index] = j
            if self.isValid(col_indexes, cur_row_index, j):
                self.backTrack(n, results, cur_row_index + 1, col_indexes)

    def isValid(self, col_indexes, i, j):
        for k in range(i):
            if col_indexes[k] == j or abs(i - k) == abs(col_indexes[i] - col_indexes[k]):
                return False
        return True