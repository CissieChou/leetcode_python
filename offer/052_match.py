# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        momo = {}
        def dp(i, j):
            if (i, j) not in momo:
                if j == len(pattern):
                    ans = (i == len(s))
                else:
                    firstMatch = i < len(s) and pattern[j] in {s[i], "."}

                    if j + 1 < len(pattern) and pattern[j+1] == "*":
                        ans = dp(i, j+2) or (firstMatch and dp(i+1, j))
                    else:
                        ans = dp(i+1, j+1) and firstMatch

                momo[(i, j)] = ans

            return momo[(i, j)]

        return dp(0, 0)
