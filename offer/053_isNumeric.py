# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        import re
        if re.match(r"[+-]?\d*(\.\d+)?([eE][+-]?\d+)?", s):
            return True
        else:
            return False

if __name__ == '__main__':
    solution = Solution()
    print (solution.isNumeric("12e"))
    import re
    pattern = re.compile("o")
    print (pattern.match("dog"))