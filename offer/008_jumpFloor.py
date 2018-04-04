# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here

        if number <= 0:
            return 0
        if number <= 2:
            return number
        pre = 1
        tail = 2

        for index in range(3, number+1):
            temp = pre + tail
            pre = tail
            tail = temp

        return tail