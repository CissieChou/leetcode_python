from  __future__ import print_function
class Solution(object):
    '''
    Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
    '''
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for row_index in range(length/2):
            for col_index in range(length):
                temp = matrix[row_index][col_index]
                matrix[row_index][col_index] = matrix[length - row_index - 1][col_index]
                matrix[length - row_index - 1][col_index] = temp

        for row_index in range(length):
            for col_index in range(row_index +1, length):
                temp = matrix[row_index][col_index]
                matrix[row_index][col_index] = matrix[col_index][row_index]
                matrix[col_index][row_index] = temp

if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    solution = Solution()
    solution.rotate(matrix)
    print (matrix)