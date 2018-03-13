class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return
        for i in range(len(board)):
            self.walk(board, i, 0)
            self.walk(board, i, len(board[0]) - 1)
        for j in range(len(board[0])):
            self.walk(board, 0, j)
            self.walk(board, len(board) - 1, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "1":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"

    def walk(self, board, i, j):
        if board[i][j] == "X" or board[i][j] == "1":
            return

        board[i][j] = "1"
        if i >= 1:
            self.walk(board, i - 1, j)
        if j >= 1:
            self.walk(board, i, j - 1)
        if i < len(board) - 1:
            self.walk(board, i + 1, j)
        if j < len(board[0]) - 1:
            self.walk(board, i, j + 1)
