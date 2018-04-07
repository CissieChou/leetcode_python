# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        temp_result = 0
        for num in array:
            temp_result ^= num

        one_index = -1

        for index in range(32):
            if ((temp_result >> index)& 1) == 1:
                one_index = index
                break

        first_result = 0
        second_result = 0

        for num in array:
            if ((num >> one_index) & 1) == 1:
                first_result ^= num
            else:
                second_result ^= num

        return [first_result, second_result]
