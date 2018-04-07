# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # write code here
        if num2 == 0:
            return num1

        carry = (num1 & num2) << 1
        temp_sum = (num1 ^ num2)

        return self.Add(temp_sum, carry)