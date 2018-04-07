# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if len(s.strip()) == 0:
            return s
        return " ".join([word for word in reversed(s.split())])
