class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        row = len(board)
        if row == 0:
            return
        col = len(board[0])
        if row == 0 or col == 0:
            return

        for i in range(row):
            self.walk(board, i, 0)
            self.walk(board, i, col - 1)
        for j in range(col):
            self.walk(board, 0, j)
            self.walk(board, row - 1, j)

        for i in range(row):
            for j in range(col):
                if board[i][j] == "1":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"

    def walk(self, board, i, j):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        if board[i][j] in {"X", "1"}:
            return
        board[i][j] = "1"
        self.walk(board, i - 1, j)
        self.walk(board, i + 1, j)
        self.walk(board, i, j - 1)
        self.walk(board, i, j + 1)
