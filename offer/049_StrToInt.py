# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        s = s.strip()
        neg = False
        if s.startswith("+"):
            s = s[1:]
        elif s.startswith("-"):
            s = s[1:]
            neg = True

        for ch in s:
            if not ch.isdigit():
                return 0

        number = 0

        for ch in s:
            number = number*10
            number += int(ch)

        if neg:
            number = -number

        return number