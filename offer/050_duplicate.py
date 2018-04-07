# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        number_count_dict = {}
        for number in numbers:
            if number not in number_count_dict:
                number_count_dict[number] = 1
            else:
                duplication[0] = number
                return True
        return False
