# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here

        if n == 0:
            return 0
        if n <= 2:
            return 1

        pre = 1
        tail = 1

        for index in range(3, n + 1):
            temp = pre + tail
            pre = tail
            tail = temp
        return tail