# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        result = numbers[0]
        count = 1
        for number in numbers[1:]:
            if count == 0:
                result = number
                count += 1
            elif number == result:
                count += 1
            else:
                count -= 1
        count = 0
        for number in numbers:
            if number == result:
                count += 1
        if count > len(numbers)/2:
            return result
        else:
            return 0

