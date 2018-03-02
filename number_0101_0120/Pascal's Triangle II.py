class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        if rowIndex == 1:
            result = [1]
        elif rowIndex == 2:
            result = [1, 1]
        else:
            result = [0] * (rowIndex - 2) + [1, 1]

        for index in range(3, rowIndex + 1):
            pre_num = result[-1]
            for col_index in range(2, index + 1):
                cur_num = result[-col_index]
                result[-col_index] = cur_num + pre_num
                pre_num = cur_num

        return result