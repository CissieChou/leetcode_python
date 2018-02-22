class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        row_length = len(matrix)
        col_length = len(matrix[0])
        count = 0
        total_count = row_length * col_length

        cycle = 0
        result = []
        while count < total_count:
            print count
            for index in range(cycle, col_length - cycle):
                print index
                result.append(matrix[cycle][index])
                count += 1

            for index in range(cycle + 1, row_length - cycle):
                result.append(matrix[index][col_length - cycle - 1])
                count += 1

            if count >= total_count:
                break

            for index in range(col_length - cycle - 2, cycle - 1, -1):
                result.append(matrix[row_length - cycle - 1][index])
                count += 1

            for index in range(row_length - cycle - 2, cycle, -1):
                result.append(matrix[index][cycle])
                count += 1

            cycle += 1

        return result

if __name__ == '__main__':
    length = 4
    matrix = []

    count = 0

    for i in range(length):
        matrix.append([])
        for j in range(length):
            count += 1
            matrix[-1].append(count)

    matrix = [[3], [2]]
    solution = Solution()
    print solution.spiralOrder(matrix)
