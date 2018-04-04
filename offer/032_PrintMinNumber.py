# -*- coding:utf-8 -*-
class Solution:

    def PrintMinNumber(self, numbers):
        # write code here
        numbers = [str(number) for number in numbers]

        def campare(x, y):
            if x + y < y + x:
                return -1
            if x + y > y + x:
                return 1
            return 0

        numbers = sorted(numbers,cmp=campare)

        result = "".join(numbers)
        return result
