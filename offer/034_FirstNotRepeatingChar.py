# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here

        result_dict = {}
        for index, ch in enumerate(s):
            if ch not in result_dict:
                result_dict[ch] = (1, index)
            else:
                result_dict[ch] = (-1, index)
        result = 1 << 31
        for value in result_dict.values():
            if value[0] == 1 and value[1] < result:
                result = value[1]
        if result == 1 << 31:
            return -1
        else:
            return result