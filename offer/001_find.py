# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here

        if len(array) == 0 or len(array[0]) == 0:
            return False

        if target < array[0][0] or target > array[-1][-1]:
            return False

        col_index = len(array[0]) - 1
        row_index = 0

        while col_index >= 0 and row_index < len(array):
            if array[row_index][col_index] == target:
                return True
            elif array[row_index][col_index] < target:
                row_index += 1
            else:
                col_index -= 1

        return False
