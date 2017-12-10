class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        result_lines = []
        for index in range(numRows):
            result_lines.append([])

        top_down_size = numRows
        down_top_count = numRows - 2
        size_epoch = top_down_size + down_top_count

        for index, ch in enumerate(s):
            result_index = index % size_epoch

            if result_index >= top_down_size:
                result_index = numRows + numRows - result_index - 2

            result_lines[result_index].append(ch)

        return "".join(["".join(result_line) for result_line in result_lines])


if __name__ == '__main__':
    solution = Solution()
    s = "PAHNAPLSIIGYIR"
    print solution.convert(s, 3)
