class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        results = [[1], [1, 1]]
        if numRows <= 2:
            return results[:numRows]

        for index in range(3, numRows + 1):
            new_row = [1]
            need_count = index - 2
            for count in range(need_count):
                new_row.append(results[-1][count] + results[-1][count+1])
            new_row.append(1)
            results.append(new_row)

        return results
