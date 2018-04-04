# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
    # write code here
        row_length = len(matrix)
        if row_length == 0:
            return []

        col_length = len(matrix[0])
        results = []

        circle_count = 0
        total_count = row_length * col_length

        count = 0
        while count < total_count:
            for index in range(circle_count, col_length - circle_count):
                results.append(matrix[circle_count][index])
                count += 1

            for index in range(circle_count+1, row_length - circle_count):
                results.append(matrix[index][col_length - circle_count - 1])
                count += 1

            if count >= total_count:
                break

            for index in range(col_length - circle_count - 2, circle_count - 1, -1):
                results.append(matrix[row_length - circle_count - 1][index])
                count += 1

            for index in range(row_length - circle_count - 2, circle_count, - 1):
                results.append(matrix[index][circle_count])
                count += 1

            circle_count += 1

        return results
if __name__ == '__main__':
    matrix = [[1],[2],[3],[4],[5]]
    solution = Solution()
    solution.printMatrix(matrix)