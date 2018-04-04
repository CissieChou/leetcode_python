# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number == 0:
            return 0

        dp = [0] * number
        dp[0] = 1
        for i in range(1, number):
            for j in range(0, i):
                dp[i] += dp[j]
            dp[i] += 1

        return dp[number-1]