from __future__ import print_function


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.check(board, word, i, j, 0):
                    return True

        return False

    def check(self, board, word, i, j, count):
        if count >= len(word):
            return False

        if i < 0 or i > len(board) - 1 or j < 0 or j > len(board[0]) - 1:
            return False

        if not word[count] == board[i][j]:
            return False
        elif word[count] == board[i][j] and count == len(word) - 1:
            return True

        board[i][j] = "##" + board[i][j] + "##"
        result = self.check(board, word, i - 1, j, count + 1) or self.check(board, word, i, j - 1, count + 1) \
               or self.check(board, word, i + 1, j, count + 1) or self.check(board, word, i, j + 1, count + 1)

        board[i][j] = board[i][j].strip("#")

        return result


if __name__ == '__main__':
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "SEE"
    solution = Solution()
    print(solution.exist(board, word))
