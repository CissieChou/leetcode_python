# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        neg_flag = False
        if exponent < 0:
            neg_flag = True
            exponent = abs(exponent)

        if exponent == 0:
            return 1
        if exponent == 1:
            return base

        sub_result = self.Power(base, exponent>>1)
        result = sub_result * sub_result
        if not exponent & 1 == 0:
            result *= base

        if neg_flag:
            result = 1/ result

        return result