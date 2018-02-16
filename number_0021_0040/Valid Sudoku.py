class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        flag = True

        for i in range(9):
            if not len(set(board[i])) + board[i].count(".") == len(board[i]) + 1:
                flag = False
                break

        if flag:
            for j in range(9):
                column_list = []
                for i in range(9):
                    column_list.append(board[i][j])

                if not len(set(column_list)) + column_list.count(".") == len(column_list) + 1:
                    flag = False
                    break

        if flag:
            for i in range(0, 9 - 2, 3):
                for j in range(0, 9 - 2, 3):
                    matrix_list = []
                    for i_add in range(3):
                            for j_add in range(3):
                                matrix_list.append(board[i+i_add][j+j_add])

                    if not len(set(matrix_list)) + matrix_list.count(".") == len(matrix_list) + 1:
                        flag = False
                        break

        return flag

if __name__ == '__main__':
    board = [[".","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]]
    solution = Solution()
    print (solution.isValidSudoku(board))