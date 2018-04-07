# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if len(s) == 0:
            return ""
        temp_s = s + s

        n %= len(s)

        return temp_s[n:n + len(s)]
    