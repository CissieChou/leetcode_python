class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        results = []
        for index in range(n):
            results.append([-1] * n)

        count = 0
        total_count = n * n
        cycle = 0
        while count < total_count:
            for index in range(cycle, n - cycle):
                count += 1
                results[cycle][index] = count

            for index in range(cycle + 1, n - cycle):
                count += 1
                results[index][n - cycle - 1] = count

            if count >= total_count:
                break

            for index in range(n - cycle - 2, cycle - 1, -1):
                count += 1
                results[n - cycle - 1][index] = count

            for index in range(n - cycle - 2, cycle, -1):
                count += 1
                results[index][cycle] = count

            cycle += 1

        return results

if __name__ == '__main__':
    n = 4
    solution = Solution()

    matrix = solution.generateMatrix(n)
    for row in matrix:
        print row
