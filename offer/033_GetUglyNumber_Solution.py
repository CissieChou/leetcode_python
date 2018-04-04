# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 0:
            return 0
        dp = [1] * index
        index_2 = 0
        index_3 = 0
        index_5 = 0

        for i in range(1, index):
            dp[i] = min(dp[index_2]*2, dp[index_3]*3, dp[index_5]*5)

            while dp[index_2]*2 <= dp[i]:
                index_2 += 1
            while dp[index_3]*3 <= dp[i]:
                index_3 += 1
            while dp[index_5]*5 <= dp[i]:
                index_5 += 1

        return dp[index - 1]